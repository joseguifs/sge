from django.contrib import admin
from .models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','category','brand','description','serial_number','cost_price','selling_price','quantity','created_at','update_at']
    search_fields = ['id','title','category__name','brand__name','description','serial_number','cost_price','selling_price','quantity','created_at','update_at']