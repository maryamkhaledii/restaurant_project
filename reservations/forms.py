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

        if date and time:
            from datetime import datetime
            dt = datetime.combine(date, time)
            if dt < timezone.now():
                raise forms.ValidationError("زمان گذشته معتبر نیست")

        return cleaned
