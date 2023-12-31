# Generated by Django 4.2.3 on 2023-07-28 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servidores', '0001_initial'),
        ('databases', '0001_initial'),
        ('sistemas', '0002_sistema_siglas'),
        ('componentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='database',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='databases.database'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='servidor',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='servidores.servidor'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='sistema',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='sistemas.sistema'),
        ),
    ]
