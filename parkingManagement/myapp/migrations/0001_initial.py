# Generated by Django 5.0.4 on 2024-04-27 03:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Paark",
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
                ("noplate", models.CharField(max_length=50)),
                (
                    "modifiednoplate",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("engine_number", models.CharField(max_length=20)),
                ("chassis_number", models.CharField(max_length=20)),
                ("insurance_details", models.TextField()),
                ("contact_number", models.CharField(max_length=15)),
                ("email_address", models.EmailField(max_length=254)),
                ("owner", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=50)),
                ("bluebook_expiry_date", models.DateField()),
                ("category", models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name="Park",
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
                ("noplate", models.CharField(max_length=50)),
                (
                    "modifiednoplate",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("engine_number", models.CharField(max_length=20)),
                ("chassis_number", models.CharField(max_length=20)),
                ("insurance_details", models.TextField()),
                ("contact_number", models.CharField(max_length=15)),
                ("email_address", models.EmailField(max_length=254)),
                ("car_owner", models.CharField(max_length=100)),
                ("car_color", models.CharField(max_length=50)),
                ("bluebook_expiry_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Pi",
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
                ("pic", models.ImageField(blank=True, null=True, upload_to="")),
                ("iii", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="FineDetail",
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
                ("vehicle_number", models.CharField(max_length=100)),
                ("owner_email", models.EmailField(max_length=100)),
                ("owner_name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("time", models.TimeField()),
                ("fine_types", models.CharField(max_length=255)),
                ("other_fine", models.TextField(blank=True)),
                (
                    "common_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("fine_reason", models.CharField(blank=True, max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("paid", models.BooleanField(default=False)),
                (
                    "traffic_officer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tasbir",
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
                ("tasbir", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
