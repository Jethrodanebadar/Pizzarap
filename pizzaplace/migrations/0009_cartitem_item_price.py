# Generated by Django 5.0.6 on 2024-06-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaplace', '0008_alter_cartitem_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='item_price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6),
        ),
    ]
