# Generated by Django 5.0.3 on 2024-03-31 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("day_plan", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="meal",
            old_name="date",
            new_name="meal_date",
        ),
    ]
