# Generated by Django 3.2.18 on 2023-04-16 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demandas', '0010_alter_novademanda_usuario_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novademanda',
            name='setor_demanda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demandas.setor'),
        ),
        migrations.AlterField(
            model_name='novademanda',
            name='usuario_criacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
