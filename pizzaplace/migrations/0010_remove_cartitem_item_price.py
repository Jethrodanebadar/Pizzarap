# Generated by Django 5.0.6 on 2024-06-03 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaplace', '0009_cartitem_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='item_price',
        ),
    ]
