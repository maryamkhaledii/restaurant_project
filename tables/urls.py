from django.urls import path
from .views import (
    table_list, table_detail,
    table_create, table_update, table_delete
)

urlpatterns = [
    path("", table_list, name="table_list"),
    path("<int:pk>/", table_detail, name="table_detail"),
    path("create/", table_create, name="table_create"),
    path("<int:pk>/update/", table_update, name="table_update"),
    path("<int:pk>/delete/", table_delete, name="table_delete"),
]
