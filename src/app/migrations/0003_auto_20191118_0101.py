# Generated by Django 2.2.7 on 2019-11-18 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_employee_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='package',
            name='image',
        ),
    ]