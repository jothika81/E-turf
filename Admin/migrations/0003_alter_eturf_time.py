# Generated by Django 5.0.1 on 2024-08-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_eturf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eturf',
            name='Time',
            field=models.TimeField(),
        ),
    ]