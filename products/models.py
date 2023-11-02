"""
Products App - Models
----------------
Models for Products App.
"""
from django.db import models
from django_resized import ResizedImageField


class Category(models.Model):
    """Category model"""

    class Meta:
        """Override Meta class"""

        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """Method that returns category friendly_name"""
        return self.friendly_name


class Product(models.Model):
    """Product model"""

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=False, blank=False)
    type = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField()
    code = models.CharField(max_length=6, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='media/', force_format='WEBP',null=True, blank=True)
    stock = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.name)
