# Generated by Django 4.2.4 on 2023-08-29 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="author_data",
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
                ("author_id", models.IntegerField()),
                ("student_name", models.CharField(max_length=255)),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("KVS", "KITHABU  WA SUNNA"),
                            ("AQD", "AQEEDA"),
                            ("USR", "FIQHUL USRA"),
                            ("MUL", "FIQHUL MUAMALA"),
                            ("LUG", "LUGA WAL ADAB"),
                            ("TRQ", "THAREEQ WAL HALARA"),
                        ],
                        max_length=3,
                    ),
                ),
                ("batch", models.IntegerField(default=7)),
            ],
        ),
        migrations.CreateModel(
            name="blog_write",
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
                ("author_id", models.IntegerField()),
                ("heading", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("image", models.ImageField(upload_to=None)),
                ("publishing_date", models.DateField()),
            ],
        ),
    ]
