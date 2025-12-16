from django.urls import path
from . import views

app_name = "tables"

urlpatterns = [
    path("", views.table_list, name="list"),
    path("<int:pk>/", views.table_detail, name="detail"),
    path("create/", views.table_create, name="create"),
    path("<int:pk>/update/", views.table_update, name="update"),
    path("<int:pk>/delete/", views.table_delete, name="delete"),
]


