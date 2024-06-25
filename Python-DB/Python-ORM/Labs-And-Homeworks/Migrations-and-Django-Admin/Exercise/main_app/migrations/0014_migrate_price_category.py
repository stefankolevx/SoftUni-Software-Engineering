# Generated by Django 5.0.4 on 2024-06-25 19:51

from django.db import migrations


def set_price(apps, schema_editor):
    MULTIPLIER = 120

    smartphone_model = apps.get_model("main_app", "SmartPhone")

    for smartphone in smartphone_model.objects.all():
        smartphone.price = MULTIPLIER * len(smartphone.brand)
        smartphone.save()


def set_category(apps, schema_editor):
    smartphone_model = apps.get_model("main_app", "SmartPhone")

    for smartphone in smartphone_model.objects.all():
        if smartphone.price >= 750:
            smartphone.category = "Expensive"
        else:
            smartphone.category = "Cheap"

        smartphone.save()


def reverse_fulling_of_columns_category_and_price(apps, schema_editor):
    smartphone_model = apps.get_model("main_app", "SmartPhone")

    for smartphone in smartphone_model.objects.all():
        smartphone.category = smartphone_model._meta.get_field('category').default
        smartphone.price = smartphone_model._meta.get_field('price').default
        smartphone.save()


def set_all_columns(apps, schema_editor):
    set_price(apps, schema_editor)
    set_category(apps, schema_editor)

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_all_columns, reverse_fulling_of_columns_category_and_price)
    ]
