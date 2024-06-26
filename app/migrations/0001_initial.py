# Generated by Django 4.1.13 on 2024-06-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Messages",
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
                ("Name", models.CharField(max_length=100)),
                ("Email", models.EmailField(max_length=100)),
                ("Subject", models.CharField(max_length=100)),
                ("Message", models.TextField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="My_Service",
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
                ("short_intro", models.TextField(blank=True, max_length=2000)),
                ("logo", models.ImageField(null=True, upload_to="services/")),
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="My_Works",
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
                ("fields", models.CharField(max_length=50)),
                ("short_intro", models.TextField(blank=True, max_length=2000)),
                ("logo", models.ImageField(null=True, upload_to="Portfolio/")),
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Personal_About_Me",
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
                ("Name", models.CharField(max_length=100)),
                ("Short_intro", models.TextField(blank=True, max_length=2000)),
                ("Birthday", models.DateField()),
                ("Age", models.IntegerField()),
                ("Website", models.CharField(max_length=100)),
                ("Degree", models.CharField(max_length=13)),
                ("PhEmailone", models.EmailField(max_length=254)),
                ("City", models.CharField(max_length=200)),
                ("Address", models.CharField(max_length=200)),
                ("Email", models.CharField(max_length=200)),
                ("Call", models.CharField(max_length=200)),
                ("Freelance", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Professional_About_Me",
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
                ("Happy_Clients", models.IntegerField()),
                ("Projects", models.IntegerField()),
                ("Hours_Of_Support", models.IntegerField()),
                ("Awards", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Testimonials",
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
                ("short_intro", models.TextField(blank=True, max_length=2000)),
                ("Image", models.ImageField(null=True, upload_to="Testimonials/")),
                ("roal", models.CharField(max_length=50)),
            ],
        ),
    ]
