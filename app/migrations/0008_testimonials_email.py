# Generated by Django 4.1.13 on 2024-06-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_rename_fields_my_works_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="testimonials",
            name="email",
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]