"""
Bag App - Views
----------------
Views for Bag App.
"""

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, View, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponse

from products.models import Product


class Bag(UserPassesTestMixin, TemplateView):
    """A view that will render the bag page template"""

    template_name = "bag/bag.html"

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True


class AddToBag(UserPassesTestMixin, View):
    """A view that add the product and the corresponding quantity to the
    shopping bag"""

    template_name = "bag/bag.html"

    def post(self, request, product_id):
        """Override post method"""
        product = get_object_or_404(Product, pk=product_id)
        quantity = int(request.POST.get("quantity"))
        current_url = request.POST.get("current_url")
        bag = request.session.get("bag", {})

        if str(product_id) in list(bag.keys()):
            bag[str(product_id)] += quantity
            messages.success(request, f'Updated <b>{product.name}</b>\
                 quantity to {bag[str(product_id)]}',
                             extra_tags="bag_add safe")
        else:
            bag[product_id] = quantity
            messages.success(request, f'Added <b>{product.name}</b>\
                 to your bag', extra_tags="bag_add safe")
        request.session["bag"] = bag
        return redirect(current_url)

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True


class RemoveFromBag(UserPassesTestMixin, DeleteView):
    """A view that deletes the product from the shoping bag"""

    template_name = "bag/bag.html"

    def delete(self, request, product_id):
        """Override post method"""
        try:
            product = get_object_or_404(Product, pk=product_id)
            current_url = request.POST.get('current_url')
            bag = request.session.get('bag', {})

            if str(product_id) in list(bag.keys()):
                del bag[str(product_id)]
                messages.success(
                    request, f'<b>{product.name}</b> was removed from\
                     your shopping bag', extra_tags='safe')
            else:
                messages.error(
                    request, f'<b>{product.name}</b> was not found in the\
                     shopping bag. Delete action failed', extra_tags='safe')
            request.session['bag'] = bag
            return redirect(current_url)

        except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True


class IncrementQuantity(UserPassesTestMixin, View):
    """A view that updates the product quantity by incrementing
    the value with 1"""

    template_name = "bag/bag.html"

    def post(self, request, product_id):
        """Override post method"""
        product = get_object_or_404(Product, pk=product_id)
        current_url = request.POST.get("current_url")
        bag = request.session.get("bag", {})

        if str(product_id) in list(bag.keys()):
            if bag[str(product_id)] < product.stock:
                bag[str(product_id)] += 1
                messages.success(
                    request, f'The quantity for <b>{product.name}</b>\
                     was updated to {bag[str(product_id)]}', extra_tags="safe")
            else:
                messages.info(
                    request, f'Limited stock. Cannot order more than\
                     {bag[str(product_id)]} items for <b>{product.name}</b>',
                    extra_tags='safe')
        else:
            messages.error(
                request,
                f"{product.name} is not in your bag.\
                           Quantity update failed",
            )
        request.session["bag"] = bag
        return redirect(current_url)

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True


class DecrementQuantity(UserPassesTestMixin, View):
    """A view that updates the product quantity by decrementing
    the value with 1"""

    template_name = "bag/bag.html"

    def post(self, request, product_id):
        """Override post method"""
        product = get_object_or_404(Product, pk=product_id)
        current_url = request.POST.get("current_url")
        bag = request.session.get("bag", {})

        if str(product_id) in list(bag.keys()):
            if bag[str(product_id)] > 1:
                bag[str(product_id)] -= 1
                messages.success(
                    request, f'The quantity for <b>{product.name}</b>\
                    was updated to {bag[str(product_id)]}', extra_tags="safe")
        else:
            messages.error(
                request, f'<b>{product.name}</b> is not in your bag.\
                        Quantity update failed', extra_tags='safe')
        request.session["bag"] = bag
        return redirect(current_url)

    def test_func(self):
        if self.request.user.is_authenticated:
            return not self.request.user.is_superuser
        return True
