# Generated by Django 3.2.21 on 2023-11-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0007_auto_20231030_2253"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateTimeField(default="2023-11-07 12:14:14"),
        ),
    ]
