# Generated by Django 3.2.21 on 2023-10-30 22:53

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="default_phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=20, null=True, region=None
            ),
        ),
    ]
