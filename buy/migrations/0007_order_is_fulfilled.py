# Generated by Django 5.1.6 on 2025-07-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0006_alter_order_cus_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_fulfilled',
            field=models.BooleanField(default=False),
        ),
    ]
