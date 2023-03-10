# Generated by Django 4.1.4 on 2023-01-12 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("website", "0006_order_customer_credit_service_credit_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="cash_credit",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
