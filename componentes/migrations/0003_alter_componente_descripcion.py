# Generated by Django 4.2.3 on 2023-08-05 22:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0002_alter_componente_database_alter_componente_servidor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
    ]