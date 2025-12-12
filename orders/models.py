from django.db import models
from tables.models import Table
from foods.models import Food

class Order(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return f"Order #{self.id} - Table {self.table.number}"


