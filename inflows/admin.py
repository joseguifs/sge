from django.contrib import admin
from .models import Inflow
# Register your models here.
@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ['id','supplier','product','created_at','update_at']
    search_fields = ['id','supplier__name','product__title','update_at']