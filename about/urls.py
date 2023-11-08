"""
About App - URLS
----------------
URLS Configuration for About App
"""
from django.urls import path
from . import views

urlpatterns = [
    path("about/", About.Contact.as_view(), name="about"),
]
