# Generated by Django 5.0.4 on 2024-06-25 20:02

from django.db import migrations
from django.utils import timezone


def update_delivery_and_warranty(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')

    for order in order_model.objects.all():
        if order.status == "Pending":
            order.delivery = order.order_date + timezone.timedelta(days=3)
            order.save()
        elif order.status == "Completed":
            order.warranty = "24 months"
            order.save()
        elif order.status == "Canceled":
            order.delete()


def reverse_delivery_and_warranty(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')

    for order in order_model.objects.all():
        if order.status == "Pending":
            order.delivery = None
        elif order.status == "Completed":
            order.warranty = order_model._meta.get_field('warranty').default

        order.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_migrate_price_category'),
    ]

    operations = [
        migrations.RunPython(update_delivery_and_warranty, reverse_delivery_and_warranty)
    ]
