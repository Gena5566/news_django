# Generated by Django 5.0 on 2023-12-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mynewsapp", "0004_allnews_is_active_alter_allnews_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
        ),
    ]
