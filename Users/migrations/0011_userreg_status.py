# Generated by Django 5.0.1 on 2024-09-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_rename_bookingpackage_booking_turfname'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
