from django import forms
from django.utils import timezone
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "phone", "date", "time", "num_people", "table"]

    def clean(self):
        cleaned = super().clean()
        date = cleaned.get("date")
        time = cleaned.get("time")
        table = cleaned.get("table")
        num_people = cleaned.get("num_people")

        # اگر تاریخ و ساعت را وارد نکرده بود، ادامه نده
        if date and time:
            reservation_datetime = timezone.make_aware(
                timezone.datetime.combine(date, time)
            )

            # مقایسه صحیح با timezone-aware datetime
            if reservation_datetime < timezone.now():
                raise forms.ValidationError("Reservation time cannot be in the past.")

        # چک ظرفیت میز
        if table and num_people:
            if num_people > table.seats:
                raise forms.ValidationError(f"Selected table only has {table.seats} seats.")

        return cleaned

