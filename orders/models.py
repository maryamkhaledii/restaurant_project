from django.conf import settings
from django.db import models
from foods.models import Food


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "در انتظار تایید"),
        ("confirmed", "تایید شده"),
        ("preparing", "در حال آماده‌سازی"),
        ("done", "آماده تحویل"),
        ("canceled", "لغو شده"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )
    total_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.food.name} x {self.quantity}"








