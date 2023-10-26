"""
Products App - Views
----------------
Views for Products App.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from .models import Product, Category
import urllib
import json
from django.db.models import F
from products.forms import UpdateProductForm
from products.models import Product, Category
from product_reviews.forms import ReviewForm, UpdateReviewForm
from product_reviews.models import Review as ReviewModel
from wishlist.forms import SetWishlistRelation
from wishlist.models import WishlistLine


class Products(ListView):
    """A view to show all products, including sorting and search queries"""

    template_name = "products/products.html"
    model = Product
    paginate_by = 12
    context_object_name = "products"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["products"] = Product.objects.all().order_by("type")
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
            if sortkey != "best_sellers" and "rating" not in sortkey:
                products = products.order_by(sortkey)
            elif "rating" in sortkey:
                if direction == "asc":
                    products = products.order_by(F("rating").asc(nulls_last=True))
                elif direction == "desc":
                    products = products.order_by(F("rating").desc(nulls_last=True))

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
            if is_filter is True and key in filter_options:
                del parameters[key]
        if parameters:
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


class ProductDetail(ListView):
    """A view to show a product details including reviews"""

    template_name = "products/product_details.html"

    def get(self, request, product_id):
        """Override get method"""
        product = get_object_or_404(Product, pk=product_id)
        current_review = None
        current_wishlist_line = None
        if (
            request.user.is_authenticated
            and len(
                ReviewModel.objects.filter(
                    Q(author=request.user) & Q(product=product))
            )
            == 1
        ):
            current_review = ReviewModel.objects.get(
                author=self.request.user, product=product
            )
        update_product_form = UpdateProductForm(
            instance=product,
            initial={"category": product.category.get_friendly_name()},
            prefix="UPDATE",
        )

        if (
            self.request.user.is_authenticated
            and WishlistLine.objects.filter(
                Q(user=self.request.user) & Q(product=product)
            ).exists()
        ):
            current_wishlist_line = WishlistLine.objects.get(
                user=self.request.user, product=product
            )

        add_to_wishlist_form = SetWishlistRelation(data=request.GET)
        context = {
            "product": product,
            "update_product_form": update_product_form,
            "review_form": ReviewForm,
            "update_review_form": UpdateReviewForm(instance=current_review),
            "review_list": ReviewModel.objects.filter(
                product=product).order_by(
                "-date_updated_on"
            ),
            "current_review": current_review,
            "add_to_wishlist_form": add_to_wishlist_form,
            "current_wishlist_line": current_wishlist_line,
        }

        return render(request, "products/product_detail.html", context)


class ProductAddViewAdmin(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    A view that provides a form to add a new Product entry
    """

    model = Product
    template_name = "base.html"

    fields = [
        "category",
        "sku",
        "name",
        "type",
        "description",
        "price",
        "code",
        "image",
        "stock",
    ]

    def post(self, request):
        form_error = None
        if request.method == "POST":
            add_product_form = UpdateProductForm(
                request.POST, request.FILES, prefix="ADD"
            )

            if add_product_form.is_valid():
                add_product_form.save()
                messages.success(
                    request, "A new product was successfully added to \
                         the database"
                )
                return redirect("products")
            else:
                messages.error(
                    request,
                    "There was a problem when trying to add"
                    + " a new product to  database. Please try again!",
                )
                return redirect("products")
        else:
            add_product_form = AddUpdateProductForm(request.GET, prefix="ADD")
            context = {
                "form_error": form_error,
            }
        return render(request, "products.html", context)

    def get(self, *args, **kwargs):
        """Override GET request to redirect to products details page"""
        return redirect("products")

    def test_func(self):
        return self.request.user.is_superuser


class ProductUpdateViewAdmin(LoginRequiredMixin,
                             UserPassesTestMixin, UpdateView):

    """
    A view that provides a form to update the Product entry
    coresponding to the authenticated user
    """

    model = Product
    template_name = "product_detail.html"

    fields = [
        "category",
        "sku",
        "name",
        "type",
        "description",
        "price",
        "code",
        "image",
        "stock",
    ]

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form_error = None
        if request.method == "POST":
            update_product_form = UpdateProductForm(
                request.POST, request.FILES, instance=product, prefix="UPDATE"
            )

            if update_product_form.is_valid():
                update_product_form.save()
                messages.success(
                    request, "Your product was successfully updated")
                return redirect("/products/product_details/" + str(product.pk))
            else:
                messages.error(
                    request,
                    "There was a problem when trying to update"
                    + " product details. Please try again!",
                )
                return redirect("/products/product_details/" + str(product.pk))
        else:
            update_product_form = UpdateProductForm(
                instance=product, prefix="UPDATE")

        context = {
            "update_product_form": update_product_form,
            "product": product,
            "form_error": form_error,
        }

        return render(request, "product_details.html", context)

    def get_success_url(self):
        id_key = self.get_object().id
        return "/products/product_details/" + str(id_key)

    def get(self, *args, **kwargs):
        """Override GET request to redirect to products details page"""
        return redirect("products")

    def test_func(self):
        return self.request.user.is_staff


class ProductDeleteViewAdmin(LoginRequiredMixin,
                             UserPassesTestMixin, DeleteView):
    """
    A view that deletes a product entry from the database.
    The action is performed only if the authenticated user
    is an admin.
    """

    model = Product
    success_url = reverse_lazy("products")
    template_name = "product_detail"
    success_message = "Product was successfully deleted from database."

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        """Override GET request to redirect to products page"""
        return redirect("products")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
