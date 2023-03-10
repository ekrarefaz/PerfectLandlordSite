from django.contrib import admin

from .models import Property, SavedProperty

admin.site.register(Property)
admin.site.register(SavedProperty)