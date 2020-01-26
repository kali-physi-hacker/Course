# Generated by Django 2.2.7 on 2020-01-21 09:33

import course.models.employee
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20191224_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='course_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=course.models.employee.upload_image_path),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
