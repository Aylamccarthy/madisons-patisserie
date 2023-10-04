"""
Products App - Views
----------------
Views for Products App.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from .models import Product, Category
import urllib
import json


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


class ProductDetail(ListView):
    """A view to show a product details including reviews"""

    template_name = "products/product_details.html"

    def get(self, request, product_id):
        """Override get method"""
        product = get_object_or_404(Product, pk=product_id)
        current_review = None
        current_wishlist_line = None

        if request.user.is_authenticated and len(
            ReviewModel.objects.filter(
                Q(author=request.user) & Q(product=product))) == 1:
            current_review = ReviewModel.objects.get(
                author=self.request.user, product=product)

        if self.request.user.is_authenticated and \
            WishlistLine.objects.filter(
                Q(user=self.request.user) & Q(product=product)).exists():
            current_wishlist_line = WishlistLine.objects.get(
                user=self.request.user, product=product)

        # add_to_wishlist_form = SetWishlistRelation(data=request.GET)
        context = {
            'product': product,
            # 'update_product_form': update_product_form,
            # 'review_form': ReviewForm,
            # 'update_review_form': UpdateReviewForm(instance=current_review),
            # 'review_list': ReviewModel.objects.filter(
            #     product=product).order_by('-date_updated_on'),
            # 'current_review': current_review,
            # 'add_to_wishlist_form': add_to_wishlist_form,
            # 'current_wishlist_line': current_wishlist_line,
            # 'product_json': serialize('json', Product.objects.filter(pk=product.pk)),
        }

        return render(request, "products/product_detail.html", context)
