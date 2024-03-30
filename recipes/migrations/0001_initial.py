# Generated by Django 5.0.3 on 2024-03-30 13:02

import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300)),
                (
                    "instructions",
                    djrichtextfield.models.RichTextField(max_length=10000),
                ),
                ("ingredients", djrichtextfield.models.RichTextField(max_length=10000)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[400, None],
                        upload_to="recipes/",
                    ),
                ),
                (
                    "meal_type",
                    models.CharField(
                        choices=[
                            ("breakfast", "Breakfast"),
                            ("snack", "Snack"),
                            ("lunch", "Lunch"),
                            ("dinner", "Dinner"),
                        ],
                        default="breakfast",
                        max_length=50,
                    ),
                ),
                (
                    "cuisine_types",
                    models.CharField(
                        choices=[
                            ("czech", "Czech"),
                            ("slovak", "Slovak"),
                            ("french", "French"),
                            ("thai", "Thai"),
                            ("italian", "Italian"),
                            ("chinese", "Chinese"),
                            ("indian", "Indian"),
                            ("korean", "Korean"),
                            ("vietnamese", "Vietnamese"),
                            ("japanese", "Japanese"),
                            ("other", "Other"),
                        ],
                        default="czech",
                        max_length=50,
                    ),
                ),
                ("calories", models.IntegerField()),
                ("posted_date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
