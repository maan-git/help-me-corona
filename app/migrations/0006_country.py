# Generated by Django 2.2.11 on 2020-03-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0005_neighborhood")]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Country name")),
                ("active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
            ],
        )
    ]
