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
    price = forms.DecimalField(min_value=0.0, max_digits=6, decimal_places=2)
    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )
    stock = forms.IntegerField(min_value=0)

    def __init__(self, *args, **kwargs):
        is_cake = kwargs.pop("is_cake", None)
        super().__init__(*args, **kwargs)
        """
        Set checkbox default value for update, add placeholders
        Set checkbox initial value, set category choices, add placeholders
        and remove auto-generated labels
        """

        if is_cake:
            self.fields["is_cake"].initial = True

        self.fields['category'].choices = [('', 'Category*')] +\
            [(cat.id, cat.friendly_name) for cat in Category.objects.all()]

        placeholders = {
            "sku": "Sku",
            "name": "Product Name",
            "code": "Code",
            "type": "Type",
            "description": "Description",
            "price": "Price",
            "stock": "Stock",
        }

        for field in self.fields:
            if field != "category" and field != "is_cake" and field != "image":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder

    def clean_category(self):
        """Method for assinging the correponding Category object to category
        field"""
        category_id = self.cleaned_data['category']
        category = Category.objects.get(pk=category_id)
        return category

    def clean_is_cake(self):
        """Method for assinging boolean value to is_cake field depending
        checkbox value"""
        cake = self.cleaned_data.get("is_cake", False)
        if cake:
            is_cake = True
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
