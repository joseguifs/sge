from django.contrib import admin
from .models import Categorie


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name']
