# Generated by Django 4.2.5 on 2024-08-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("instruments", "0002_instrument_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instrumentname",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
