# Generated by Django 4.2.7 on 2024-02-26 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("DAST_app", "0004_artwork_details_experience_details_account_type_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="artwork",
            table="Artwork",
        ),
        migrations.AlterModelTable(
            name="comment",
            table="Comment",
        ),
    ]
