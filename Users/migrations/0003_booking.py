# Generated by Django 5.0.1 on 2024-09-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('turflocation', models.TextField()),
                ('BookingPackage', models.TextField()),
                ('Time', models.TextField()),
            ],
        ),
    ]