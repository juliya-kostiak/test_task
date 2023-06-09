# Generated by Django 4.1.7 on 2023-03-30 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Keys",
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
                ("key", models.UUIDField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("block", models.BooleanField(default=False)),
                (
                    "id_org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizations.organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ключ",
                "verbose_name_plural": "Ключи",
            },
        ),
    ]
