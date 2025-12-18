from django.db import models
from django.conf import settings
from tables.models import Table

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "در انتظار"),
        ("cancelled", "لغو شده"),
        ("done", "انجام شده"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("table", "date", "time")

    def __str__(self):
        return f"{self.user} - میز {self.table.number}"
