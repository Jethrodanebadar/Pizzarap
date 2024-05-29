# Generated by Django 5.0.6 on 2024-05-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaplace', '0002_appetizer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
