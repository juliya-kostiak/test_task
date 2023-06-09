# Generated by Django 4.1.7 on 2023-03-30 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                    "name",
                    models.CharField(
                        max_length=500, verbose_name="Название организации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Организация",
                "verbose_name_plural": "Организации",
            },
        ),
    ]
