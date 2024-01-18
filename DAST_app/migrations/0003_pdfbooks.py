# Generated by Django 4.2.7 on 2024-01-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DAST_app", "0002_details_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="PDFbooks",
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
                ("title", models.CharField(max_length=100)),
                ("pdf_content", models.BinaryField()),
            ],
            options={
                "db_table": "PDFbooks",
            },
        ),
    ]