# Generated by Django 4.2.3 on 2023-07-28 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemas', '0003_alter_sistema_responsable'),
        ('smaxs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smax',
            name='sistema',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='sistemas.sistema'),
        ),
    ]
