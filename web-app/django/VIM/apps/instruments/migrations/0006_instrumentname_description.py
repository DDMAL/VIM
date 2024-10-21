# Generated by Django 4.2.5 on 2024-10-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("instruments", "0005_remove_language_wikidata_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="instrumentname",
            name="description",
            field=models.CharField(
                blank=True, help_text="Description of the instrument name"
            ),
        ),
    ]