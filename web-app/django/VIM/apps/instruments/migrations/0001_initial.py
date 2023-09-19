# Generated by Django 4.2.5 on 2023-09-19 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Instrument",
            fields=[
                (
                    "wikidata_id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("hornbostel_sachs_class", models.CharField(blank=True, max_length=50)),
                ("mimo_class", models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                ("wikidata_code", models.CharField(max_length=10, unique=True)),
                (
                    "wikidata_id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "en_label",
                    models.CharField(
                        help_text="Language label in English", max_length=50
                    ),
                ),
                (
                    "autonym",
                    models.CharField(
                        help_text="Language label in the language itself", max_length=50
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InstrumentName",
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
                ("name", models.CharField(max_length=50)),
                (
                    "source_name",
                    models.CharField(
                        help_text="Who or what called the instrument this?",
                        max_length=50,
                    ),
                ),
                (
                    "source_type",
                    models.CharField(
                        help_text="What type of source is this?", max_length=50
                    ),
                ),
                ("source_date", models.DateField(help_text="Date of source")),
                (
                    "source_description",
                    models.TextField(
                        blank=True,
                        help_text="Additional information about the source of this name.",
                    ),
                ),
                (
                    "description_language",
                    models.ForeignKey(
                        blank=True,
                        help_text="What language is Source Description written in?",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="instrument_name_description_language",
                        to="instruments.language",
                    ),
                ),
                (
                    "instrument",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="instruments.instrument",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="instruments.language",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AVResource",
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
                    "type",
                    models.CharField(
                        choices=[
                            ("audio", "Audio"),
                            ("video", "Video"),
                            ("image", "Image"),
                        ],
                        help_text="What type of resource is this?",
                        max_length=5,
                    ),
                ),
                ("format", models.CharField(max_length=50)),
                ("uri", models.URLField(max_length=250)),
                (
                    "instrument_date",
                    models.DateField(
                        blank=True, help_text="When was this instrument made?"
                    ),
                ),
                (
                    "instrument_maker",
                    models.CharField(
                        blank=True, help_text="Who made this instrument?", max_length=50
                    ),
                ),
                (
                    "instrument_description",
                    models.TextField(
                        blank=True,
                        help_text="Additional information about the instrument.",
                    ),
                ),
                (
                    "instrument",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="instruments.instrument",
                    ),
                ),
                (
                    "instrument_description_language",
                    models.ForeignKey(
                        blank=True,
                        help_text="What language is Instrument Description written in?",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="instruments.language",
                    ),
                ),
            ],
        ),
    ]
