# Generated by Django 4.2.2 on 2023-07-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=15, null=True, verbose_name='Nombre')),
                ('ip', models.CharField(blank=True, max_length=15, null=True, verbose_name='IP')),
                ('so', models.IntegerField(choices=[(1, 'Windows'), (2, 'Linux'), (3, 'Mainframe')], default='1', verbose_name='Sistema Operetivo')),
                ('tipo', models.IntegerField(choices=[(1, 'Servidor Aplicaciones'), (2, 'Base de Datos'), (3, 'Publicador')], default='1', verbose_name='Tipo')),
                ('ambiente', models.IntegerField(choices=[(1, 'Desarrollo'), (2, 'QA'), (3, 'Produccion')], default='1', verbose_name='Ambiente')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('estatus', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default='1', verbose_name='Estatus')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modificado')),
            ],
            options={
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
            },
        ),
    ]
