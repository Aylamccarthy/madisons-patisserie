"""
Profiles App - Admin
----------------
Admin configuration for Profiles App.
"""
from django.contrib import admin
from .models import UserProfile


admin.site.register(UserProfile)
