# Generated by Django 4.2.3 on 2023-08-23 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_documento_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='path',
        ),
    ]
