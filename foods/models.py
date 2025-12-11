from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="foods/", blank=True, null=True)

    def __str__(self):
        return self.name

