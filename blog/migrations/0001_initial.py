# Generated by Django 4.1.3 on 2022-11-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                (
                    "title",
                    models.CharField(
                        max_length=10, unique=True, verbose_name="ブログタイトル"
                    ),
                ),
                ("content", models.TextField(max_length=5000, verbose_name="本文")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog_images/",
                        verbose_name="画像",
                    ),
                ),
            ],
        ),
    ]
