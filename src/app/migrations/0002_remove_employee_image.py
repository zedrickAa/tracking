# Generated by Django 2.2.7 on 2019-11-18 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
    ]
