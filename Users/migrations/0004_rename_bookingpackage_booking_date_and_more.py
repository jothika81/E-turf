# Generated by Django 5.0.1 on 2024-09-10 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='BookingPackage',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='turflocation',
            new_name='Email',
        ),
    ]
