# Generated by Django 4.2.3 on 2023-08-05 22:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servidores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
    ]