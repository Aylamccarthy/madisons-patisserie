"""
Products App - Forms
----------------
Forms for Products App
"""
import datetime
from django import forms
from .models import Category, Product
from .widgets import CustomClearableFileInput


class UpdateProductForm(forms.ModelForm):
    """Form for update product details"""

    category = forms.ChoiceField()
    sku = forms.CharField(max_length=254)
    name = forms.CharField(max_length=254)
    type = forms.CharField(max_length=254)
    description = forms.CharField(max_length=254)
    code = forms.CharField(max_length=6)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    stock = forms.IntegerField(min_value=0)

    def __init__(self, *args, **kwargs):
        is_cake = kwargs.pop("is_cake", None)
        super().__init__(*args, **kwargs)

        if is_cake:
            self.fields["is_cake"].initial = True

        choices = [
            (category.get_friendly_name(), str(category.get_friendly_name()))
            for category in Category.objects.all()
        ]
        self.fields["category"].choices = choices

    def clean_category(self):
        """Method for assinging the correponding Category object to category
        field"""
        category_name = self.cleaned_data["category"]
        category = Category.objects.get(friendly_name=category_name)
        return category

    def clean_is_cake(self):
        """Method for assinging boolean value to is_deluxe field depending
        checkbox value"""
        cake = self.cleaned_data.get("is_cake", False)
        if cake:
            is_deluxe = True
        else:
            is_cake = False
        return is_cake

    class Meta:
        """Override Meta class"""

        model = Product
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
