from django.urls import path
from .views import food_list, food_detail, food_create

urlpatterns = [
    path("list/", food_list, name="food_list"),
    path("<int:pk>/", food_detail, name="food_detail"),
    path("create/", food_create, name="food_create"),
]