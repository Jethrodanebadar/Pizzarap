# Generated by Django 5.0.6 on 2024-06-03 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('pizzaplace', '0006_remove_cartitem_item_name_remove_cartitem_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_name', models.CharField(max_length=50)),
                ('pizza_description', models.TextField()),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('medium_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.DeleteModel(
            name='pizza_detail',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='item_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]