"""
Products App - Views
----------------
Views for Products App.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from .models import Product


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

        # CREATE DYNAMIC QUERY FOR FILTERING PRODUCTS
        filter_options = [
            "category",
            "type",
            "buttercream_cakes",
            "drip_cakes",
            "chocolate_cakes",
            "occassion_cakes",
            "desserts",
            "sweet_treats",
        ]
        filter_clauses = {}
        for key, value in request.GET.items():
            if key in filter_options:
                if key == "category":
                    filter_clauses[key] = get_object_or_404(Category, name=value)
                elif key == "cakes" or key == "everyday_essential":
                    filter_clauses[key + "__contains"] = value
                else:
                    filter_clauses[key] = value

        if filter_clauses:
            products = products.filter(**filter_clauses)

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
                | Q(cakes__icontains=query)
            )
            products = products.filter(queries)

        context = {
            "products_list": products,
            "search_term": query,
            "current_categories": categories,
        }
        return render(request, "products/products.html", context)