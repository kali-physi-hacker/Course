# Generated by Django 2.2.7 on 2019-11-18 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_trip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='emplyees',
            new_name='employees',
        ),
    ]
