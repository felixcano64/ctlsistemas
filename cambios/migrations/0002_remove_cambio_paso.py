# Generated by Django 4.2.3 on 2023-07-21 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cambios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cambio',
            name='paso',
        ),
    ]
