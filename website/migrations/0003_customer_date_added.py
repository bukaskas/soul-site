# Generated by Django 4.1.4 on 2022-12-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_alter_booking_customer_fname_alter_booking_nop"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="date_added",
            field=models.DateField(auto_now=True),
        ),
    ]
