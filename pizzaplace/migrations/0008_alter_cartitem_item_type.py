# Generated by Django 5.0.6 on 2024-06-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaplace', '0007_pizza_delete_pizza_detail_alter_cartitem_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='item_type',
            field=models.CharField(max_length=50),
        ),
    ]