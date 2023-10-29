"""
FAQs App - Admin
----------------
Admin Configuration for FAQs App.
"""
from django.contrib import admin
from faqs.models import FAQ


admin.site.register(FAQ)

 
class FAQAdmin(admin.ModelAdmin):
    """Class for displaying FAQs in admin panel"""

    list_display = (
        "question",
        "answer",
    )
