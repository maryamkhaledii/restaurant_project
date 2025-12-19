# from django.urls import path
# from . import views

# app_name = "orders"

# urlpatterns = [
#     path("create/", views.order_create, name="create"),
#     path("success/<int:order_id>/", views.order_success, name="success"),
#     path("", views.order_list, name="list"),
#     path("<int:order_id>/", views.order_detail, name="detail"),
# ]

from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("create/", views.order_create, name="create"),
    path("success/<int:order_id>/", views.order_success, name="success"),
    path("", views.order_list, name="list"),
    path("admin/", views.admin_order_list, name="admin_list"),
    path("<int:order_id>/", views.order_detail, name="detail"),
]







