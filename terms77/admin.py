from django.contrib import admin
from .models import companies, policies

# Register your models here.

admin.site.register(companies)
admin.site.register(policies)