# Generated by Django 4.2.2 on 2023-07-24 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servidores', '0001_initial'),
        ('componentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlInterna', models.CharField(blank=True, max_length=250, null=True, verbose_name='Url Interna')),
                ('urlExterna', models.CharField(blank=True, max_length=250, null=True, verbose_name='Url Externa')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('estatus', models.IntegerField(blank=True, null=True, verbose_name='Estatus')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modificado')),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='componentes.componente')),
                ('servidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servidores.servidor')),
            ],
            options={
                'verbose_name': 'url',
                'verbose_name_plural': 'urls',
            },
        ),
    ]
