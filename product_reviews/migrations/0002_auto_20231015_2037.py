# Generated by Django 3.2.21 on 2023-10-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="date_created_on",
            field=models.DateTimeField(default="2023-10-15 20:37:37"),
        ),
        migrations.AlterField(
            model_name="review",
            name="date_updated_on",
            field=models.DateTimeField(default="2023-10-15 20:37:37"),
        ),
    ]
