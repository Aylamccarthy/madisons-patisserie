"""
Products App - Views
----------------
Views for Products App.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, View, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from .models import Product, Category
import urllib
import json
from products.forms import UpdateReviewForm
from products.models import Product, Category


class Products(ListView):
    """A view to show all products, including sorting and search queries"""

    template_name = "products/products.html"
    model = Product
    paginate_by = 12
    context_object_name = "products"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["products"] = Product.objects.all()
        return context

    def get(self, request):
        products = Product.objects.all().order_by("type")
        query = None
        category = None
        filters = {}
        remove_filter = None
        sort = None
        direction = None

        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            if sortkey != "best_sellers":
                products = products.order_by(sortkey)

        if sort == "best_sellers":
            current_sorting = sort
        else:
            current_sorting = f"{sort}_{direction}"

        # CREATE DYNAMIC QUERY FOR FILTERING PRODUCTS
        filter_options = ["category", "type", "name", "description"]
        filter_clauses = {}
        for key, value in request.GET.items():
            if key in filter_options:
                if key == "category":
                    filter_clauses[key] = get_object_or_404(Category, name=value)
                elif key == "type" or key == "name":
                    filter_clauses[key + "__contains"] = value
                else:
                    filter_clauses[key] = value

        if filter_clauses:
            products = products.filter(**filter_clauses)
            for key, value in filter_clauses.items():
                if key == "category":
                    category_name = request.GET["category"]
                    category = get_object_or_404(Category, name=category_name)
                    # ADD CATEGORY FILTER TO FILTER CONTEXT
                    if "filter" in request.GET and request.get_full_path().find(
                        "filter"
                    ) < request.get_full_path().find("category"):
                        filters["category"] = (
                            "CATEGORY - " + category.get_friendly_name()
                        )
                        category = None

        # HANDLE SEARCH QUERIES
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(type__icontains=query)
            )
            products = products.filter(queries)

        # FILTER BY CATEGORY FIELD
        if "category" in request.GET:
            category_name = request.GET["category"]
            category = get_object_or_404(Category, name=category_name)
            if "filter" in request.GET and request.get_full_path().find(
                "filter"
            ) < request.get_full_path().find("category"):
                filters["category"] = "CATEGORY - " + category.get_friendly_name()

        if "filter" in request.GET:
            # ADD TYPE FILTER TO FILTER CONTEXT
            if "type" in request.GET:
                product_type = request.GET["type"]
                filters["type"] = "TYPE OF PRODUCT - " + product_type

        # ADD FILTERS LISTS TO CONTEXT FOR FILTERS DROPDOWNS
        categories = Category.objects.filter(
            id__in=products.values_list("category", flat=True).distinct()
        ).order_by("name")

        # ADD FILTER PARAMETER TO CURRENT URL ONLY ONCE
        current_url = request.get_full_path()
        if "?" in current_url:
            current_url += "&"
        else:
            current_url += "?"
        if not "filter" in current_url:
            current_url += "filter=True&"

        # REMOVE FILTERS FROM URL TO BE USED IN TEMPLATE HREFS WHEN 'CLEAR ALL' BUTTON IS ACTIVE
        # 'CLEAR ALL' BUTTON IS ACTIVE
        current_url_no_filters = request.path_info
        parameters = request.GET.copy()
        parameters_list = json.loads(json.dumps(request.GET)).items()
        is_filter = False
        for key, value in parameters_list:
            if key == "filter":
                is_filter = True
                del parameters["filter"]
            if is_filter is True and key in filter_clauses:
                del parameters[key]
        current_url_no_filters += "?" + urllib.parse.urlencode(parameters)

        # CHECK IF THERE IS ONLY ONE FILTER APPLIED AND CREATE BOOLEAN VALUE TO BE ADDED TO CONTEXT
        parameters = []
        for key, value in request.GET.items():
            parameters.append(key)
        if parameters:
            if (
                parameters[len(parameters) - 2] == "filter"
                and parameters[len(parameters) - 1] in filter_options
            ):
                remove_filter = True

            else:
                for i in range(0, len(parameters) - 2):
                    if (
                        parameters[i] == "filter"
                        and parameters[i + 1] in filter_options
                    ):
                        one_filter = True
                        for j in range(i + 2, len(parameters)):
                            if parameters[j] in filter_options:
                                one_filter = False
                                break
                        if one_filter is True:
                            remove_filter = True

        context = {
            "products": products,
            "search_term": query,
            "current_category": category,
            "categories": categories,
            "filters_list": filters,
            "current_url": current_url,
            "current_url_no_filters": current_url_no_filters,
            "remove_filter": remove_filter,
            "current_sorting": current_sorting,
            }
        return render(request, "products/products.html", context)


class ProductDetail(View):
    """ A view to show a product details including reviews """
    template_name = "products/product_details.html"

    def get(self, request, product_id):
        """Override get method"""
        product = get_object_or_404(Product, pk=product_id)
        if product.is_deluxe is True:
            update_product_form = UpdateReviewForm(
                is_deluxe=True, initial={
                    'category': product.category.get_friendly_name()
                    },
                instance=product)
        else:
            update_product_form = UpdateReviewForm(instance=product, initial={
                    'category': product.category.get_friendly_name()
                    },)
        context = {
            'product': product,
            'update_product_form': update_product_form,
        }

        return render(request, 'products/product_detail.html', context)


class ProductUpdateViewAdmin(LoginRequiredMixin, UserPassesTestMixin,
                             UpdateView):
    """
    A view that provides a form to update the Review entry
    coresponding to the authenticated user
    """

    model = Product
    template_name = "product_detail.html"

    fields = [
        'category', 'is_deluxe', 'sku', 'name', 'country', 'region',
        'grapes', 'year', 'style', 'code', 'food_pairing', 'price',
        'image', 'stock']

    def post(self, request, pk):

        product = get_object_or_404(Product, pk=pk)
        form_error = None
        if request.method == 'POST':

            update_product_form = UpdateReviewForm(
                request.POST, request.FILES, instance=product)

            if update_product_form.is_valid():
                update_product_form.save()
                messages.success(
                    request, 'Your product was successfully updated')
                return redirect('/products/product_details/' + str(product.pk))
            else:
                messages.error(
                    request, 'There was a problem when trying to update' +
                             'product details. Please try again!')
                return redirect('/products/product_details/'
                                + str(product.pk))
        else:
            update_product_form = UpdateReviewForm(instance=product)

        context = {
            'update_product_form': update_product_form,
            'product': product,
            'form_error': form_error,
        }

        return render(request, 'product_details.html', context)

    def get_success_url(self):
        id_key = self.get_object().id
        return '/products/product_details/' + str(id_key)

    def get(self, *args, **kwargs):
        """Override GET request to redirect to products details page"""
        return redirect('products')

    def test_func(self):
        return self.request.user.is_staff


class ProductDeleteViewAdmin(LoginRequiredMixin, UserPassesTestMixin,
                             DeleteView):
    """
    A view that deletes a product entry from the database.
    The action is performed only if the authenticated user
    is an admin.
    """

    model = Product
    success_url = reverse_lazy('products')
    template_name = 'product_detail'
    success_message = "Product was successfully deleted from database."

    def test_func(self):
        return self.request.user.is_staff

    def get(self, *args, **kwargs):
        """Override GET request to redirect to products page"""
        return redirect('products')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)