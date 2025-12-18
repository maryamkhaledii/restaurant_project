from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path("create/", views.reservation_create, name="create"),
    path("admin/", views.reservation_admin_list, name="admin_list"),
    path("cancel/<int:pk>/", views.reservation_cancel, name="cancel"),
    path("done/<int:pk>/", views.reservation_done, name="done"),
]






