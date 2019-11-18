# Generated by Django 2.2.7 on 2019-11-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('emplyees', models.ManyToManyField(to='tour.Employee')),
            ],
        ),
    ]
