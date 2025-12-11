from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "table", "created_at", "total_price")
    filter_horizontal = ("foods",)

