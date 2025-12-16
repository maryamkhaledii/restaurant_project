from django.urls import path
from .views import menu, food_detail, food_create, food_admin_list

app_name = "foods"

urlpatterns = [
    path("", menu, name="menu"),                 # منو برای مشتری
    path("create/", food_create, name="create"), # افزودن غذا (ادمین)
    path("admin/", food_admin_list, name="admin_list"),  # لیست غذا (ادمین)
    path("<int:pk>/", food_detail, name="detail"),
]






