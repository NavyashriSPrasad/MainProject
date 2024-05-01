# Generated by Django 4.2.7 on 2024-03-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DAST_app", "0014_remove_artconsultation_patient_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArtConsultation1",
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
                ("patient_username", models.CharField(max_length=150)),
                ("therapist_username", models.CharField(max_length=150)),
                ("artwork", models.ImageField(upload_to="artwork/")),
                ("comments", models.TextField()),
            ],
            options={
                "db_table": "ArtConsultation1",
            },
        ),
        migrations.DeleteModel(
            name="ArtConsultation",
        ),
    ]