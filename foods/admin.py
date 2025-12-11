from django.contrib import admin
from .models import Food

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    search_fields = ("name", "category")

