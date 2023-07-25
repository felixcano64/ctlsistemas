# Generated by Django 4.2.3 on 2023-07-24 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemas', '0002_sistema_siglas'),
        ('urls', '0002_alter_url_estatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='sistema',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='sistemas.sistema'),
        ),
    ]