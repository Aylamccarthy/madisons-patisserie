"""
About App - URLS
----------------
URLS Configuration for About App
"""
from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.About.as_view(), name="about"),
]
