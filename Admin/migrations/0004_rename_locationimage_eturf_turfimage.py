# Generated by Django 5.0.1 on 2024-08-31 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_alter_eturf_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eturf',
            old_name='locationimage',
            new_name='turfimage',
        ),
    ]