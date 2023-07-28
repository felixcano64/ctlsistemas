# Generated by Django 4.2.3 on 2023-07-28 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0002_alter_componente_database_alter_componente_servidor_and_more'),
        ('servidores', '0001_initial'),
        ('sistemas', '0003_alter_sistema_responsable'),
        ('urls', '0003_url_sistema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='componente',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='componentes.componente'),
        ),
        migrations.AlterField(
            model_name='url',
            name='servidor',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='servidores.servidor'),
        ),
        migrations.AlterField(
            model_name='url',
            name='sistema',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='sistemas.sistema'),
        ),
    ]
