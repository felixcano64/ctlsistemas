# Generated by Django 4.2.3 on 2023-07-21 16:45

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
                ('so', models.CharField(blank=True, max_length=20, null=True, verbose_name='Sistema Operetivo')),
                ('tipo', models.IntegerField(blank=True, null=True, verbose_name='Sistema Operetivo')),
                ('ambiente', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ambiente')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('estatus', models.IntegerField(blank=True, null=True, verbose_name='Estatus')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modificado')),
            ],
            options={
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
            },
        ),
    ]