# Generated by Django 3.2.21 on 2023-11-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_reviews", "0005_auto_20231024_1926"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="date_created_on",
            field=models.DateTimeField(default="2023-11-07 12:14:14"),
        ),
        migrations.AlterField(
            model_name="review",
            name="date_updated_on",
            field=models.DateTimeField(default="2023-11-07 12:14:14"),
        ),
    ]