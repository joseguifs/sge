from django.contrib import admin
from .models import Suppliers

@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name']
    
    # estudar esses s's aí

# Register your models here.
