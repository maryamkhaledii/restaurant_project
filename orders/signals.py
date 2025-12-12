from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def mark_table_busy(sender, instance, created, **kwargs):
    if created:
        table = instance.table
        table.is_available = False
        table.save()

@receiver(post_save, sender=Order)
def free_table_after_complete(sender, instance, **kwargs):
    if instance.status == "completed":
        table = instance.table
        table.is_available = True
        table.save()

@receiver(post_save, sender=Order)
def free_table_after_complete(sender, instance, **kwargs):
    if instance.status == "completed":
        table = instance.table
        table.is_available = True
        table.save()

