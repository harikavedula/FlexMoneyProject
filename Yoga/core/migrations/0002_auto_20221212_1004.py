# Generated by Django 2.1 on 2022-12-12 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='userid',
        ),
        migrations.DeleteModel(
            name='Reservations',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
