# Generated by Django 4.2.3 on 2023-08-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smaxs', '0002_alter_smax_sistema'),
    ]

    operations = [
        migrations.AddField(
            model_name='smax',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Requerimiento'), (2, 'Proyecto')], default='1', verbose_name='Tipo'),
        ),
    ]
