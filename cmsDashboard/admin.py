from django.contrib import admin

# Register your models here.
from .models import Common_database

# Modeli admin paneline kaydedin
admin.site.register(Common_database)