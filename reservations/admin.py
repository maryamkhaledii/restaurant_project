from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "date", "time", "num_people", "table")
    list_filter = ("date",)
    search_fields = ("name", "phone")

