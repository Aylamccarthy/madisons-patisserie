"""
About App - Views
"""
from django.views.generic import TemplateView


class About(TemplateView):
    """
    A view that only loads the about html template
    """

    template_name = "about.html"
