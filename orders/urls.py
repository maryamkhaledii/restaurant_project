from django.urls import path
from .views import order_list, order_detail, order_create

urlpatterns = [
    path("", order_list, name="order_list"),
    path("<int:pk>/", order_detail, name="order_detail"),
    path("create/", order_create, name="order_create"),
]
