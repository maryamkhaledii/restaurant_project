from django.db import models
from tables.models import Table

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    num_people = models.PositiveIntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - Table {self.table.number} @ {self.date} {self.time}"

