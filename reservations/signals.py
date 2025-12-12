from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Reservation

@receiver(post_save, sender=Reservation)
def reserve_table(sender, instance, created, **kwargs):
    if created:
        table = instance.table
        table.is_available = False
        table.save()

@receiver(post_delete, sender=Reservation)
def free_table(sender, instance, **kwargs):
    table = instance.table
    table.is_available = True
    table.save()
