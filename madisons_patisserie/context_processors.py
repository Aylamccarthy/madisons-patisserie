"""
madisons_patisserie - Context processors
"""
from django.core.serializers import serialize
from newsletter.forms import AddSubscriber
from products.forms import UpdateProductForm
from products.models import Product
from wishlist.models import WishlistLine


def add_subscription_form_to_context(request):
    """Method to return subscription form as context"""

    return {"add_subscriber_form": AddSubscriber}


def add_create_product_form_to_context(request):
    """Method to return a form for adding a new product as context"""
    return {"add_product_form": UpdateProductForm(prefix="ADD")}


def add_products_list_to_context(request):
    """Method to return a list of products as context"""
    return {"products_json": serialize("json", Product.objects.all())}


def add_wishlist_count_to_context(request):
    """Method to return a list of products as context"""
    if request.user.is_authenticated:
        return {
            "wishlist_user_count": WishlistLine.objects.filter(
                user=request.user
            ).count()
        }
    else:
        return {"wishlist_user_count": None}
