# Generated by Django 4.2.11 on 2024-05-08 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("urbanAdventurePlanner", "0002_route_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="route",
            name="length",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
