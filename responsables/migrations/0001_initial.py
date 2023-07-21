# Generated by Django 4.2.3 on 2023-07-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=60, null=True, verbose_name='Nombre')),
                ('apPaterno', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ap. Paterno')),
                ('apMaterno', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ap. Materno')),
                ('area', models.CharField(blank=True, max_length=150, null=True, verbose_name='Area')),
                ('puesto', models.CharField(blank=True, max_length=150, null=True, verbose_name='Puesto')),
                ('email', models.EmailField(blank=True, max_length=150, null=True, verbose_name='Email')),
                ('telefono', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modificado')),
            ],
            options={
                'verbose_name': 'Responsable',
                'verbose_name_plural': 'Responsables',
                'ordering': ['apPaterno', 'apMaterno', 'nombre'],
            },
        ),
    ]