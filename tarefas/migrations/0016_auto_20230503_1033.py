# Generated by Django 3.2.18 on 2023-05-03 13:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0019_remove_usuariosprojeto_fav_user_content_and_more'),
        ('tarefas', '0015_auto_20230503_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novatarefa',
            name='data_fim_planejado',
            field=models.DateField(default=datetime.datetime(2023, 5, 13, 13, 33, 16, 787513, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='UsuarioTarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.usuariosprojeto')),
            ],
        ),
    ]
