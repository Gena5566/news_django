# Generated by Django 4.2.6 on 2023-11-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AllNews",
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
                ("title", models.CharField(max_length=200)),
                ("link", models.URLField(blank=True, null=True)),
                ("time", models.DateTimeField()),
                ("image_url", models.URLField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="index")),
                ("content", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
    ]
