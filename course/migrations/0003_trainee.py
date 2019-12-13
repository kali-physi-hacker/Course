# Generated by Django 2.2.6 on 2019-12-12 15:00

import course.models.trainee
from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_employee_staff_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('surname', models.CharField(blank=True, max_length=150, null=True)),
                ('other_name', models.CharField(blank=True, max_length=150, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=course.models.trainee.upload_image_path)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('mobile_number', models.PositiveIntegerField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('date_of_enrollment', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('D', 'Done'), ('P', 'Pending')], max_length=1, null=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('summary', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
