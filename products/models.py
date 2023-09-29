"""
Products App - Models
----------------
Models for Products App.
"""
from django.db import models

# Create your models here.

class Category(models.Model):
    """Category model"""
    class Meta:
        """Override Meta class"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """Method that returns category friendly_name"""
        return self.friendly_name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    description = models.TextField()
    code = models.CharField(max_length=6)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.IntegerField(default=100)

    def __str__(self):
        return str(self.name)