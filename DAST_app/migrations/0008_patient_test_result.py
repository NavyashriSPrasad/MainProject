# Generated by Django 4.2.7 on 2024-03-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DAST_app", "0007_alter_patient_table_alter_therapist_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="Test_Result",
            field=models.CharField(max_length=50, null=True),
        ),
    ]