# Generated by Django 5.0.1 on 2024-09-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_register_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
        migrations.AddField(
            model_name='register',
            name='Gender',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='register',
            name='Managerimage',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='register',
            name='Managername',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.TextField(),
        ),
    ]
