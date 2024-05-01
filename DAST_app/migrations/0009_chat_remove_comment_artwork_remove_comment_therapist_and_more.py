# Generated by Django 4.2.7 on 2024-03-04 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("DAST_app", "0008_patient_test_result"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chat",
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
                ("message", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="art_therapy_images/"
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="DAST_app.patient",
                    ),
                ),
                (
                    "therapist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="DAST_app.therapist",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="comment",
            name="artwork",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="therapist",
        ),
        migrations.DeleteModel(
            name="Artwork",
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
