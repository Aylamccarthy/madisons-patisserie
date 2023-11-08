"""
About App - Views
"""
from django.views.generic import TemplateView


class About(TemplateView):
    """
    A view that only loads the contact html template
    """

    template_name = "about.html"
