# Generated by Django 5.0.1 on 2024-09-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_alter_eturf_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='eturf',
            name='manager',
            field=models.TextField(default=''),
        ),
    ]
