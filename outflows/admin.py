from django.contrib import admin
from .models import Outflows

@admin.register(Outflows)
class OutflowsAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','created_at','update_at']
    search_fields = ['produt__title']