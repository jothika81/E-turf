# Generated by Django 5.0.1 on 2024-09-23 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_booking_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='turfid',
            new_name='BookingPackage',
        ),
    ]
