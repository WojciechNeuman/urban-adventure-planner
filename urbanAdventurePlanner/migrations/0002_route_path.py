# Generated by Django 4.2.11 on 2024-05-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("urbanAdventurePlanner", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="route",
            name="path",
            field=models.TextField(default="{}"),
            preserve_default=False,
        ),
    ]