# Generated by Django 5.0.1 on 2024-08-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_rename_locationimage_eturf_turfimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eturf',
            name='Time',
            field=models.TextField(),
        ),
    ]
