# Generated by Django 4.2.3 on 2023-08-05 22:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cambios', '0003_alter_cambio_componente_alter_cambio_smax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cambio',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='cambio',
            name='observacion',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
    ]
