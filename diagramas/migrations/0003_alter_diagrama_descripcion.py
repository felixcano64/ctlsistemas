# Generated by Django 4.2.3 on 2023-08-05 22:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagramas', '0002_alter_diagrama_sistema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagrama',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
    ]