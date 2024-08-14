# Generated by Django 4.2.5 on 2024-08-14 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0002_instrument_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avresource',
            name='instrument',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instruments.instrument'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='default_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_image_of', to='instruments.avresource'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thumbnail_of', to='instruments.avresource'),
        ),
        migrations.AlterField(
            model_name='instrumentname',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.instrument'),
        ),
    ]
