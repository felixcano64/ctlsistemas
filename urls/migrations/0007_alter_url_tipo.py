# Generated by Django 4.2.3 on 2023-08-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0006_alter_url_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Interna'), (2, 'Externa'), (3, 'PI-PO'), (4, 'DataPower'), (5, 'ESB')], default='1', verbose_name='Tipo'),
        ),
    ]
