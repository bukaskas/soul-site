# Generated by Django 4.1.4 on 2022-12-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0004_remove_customer_date_added_customer_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="modified",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
