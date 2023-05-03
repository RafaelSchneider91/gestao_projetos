# Generated by Django 3.2.18 on 2023-05-03 12:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0004_alter_novatarefa_data_fim_realizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novatarefa',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 12, 35, 31, 822756, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='novatarefa',
            name='data_fim_planejado',
            field=models.DateField(default=datetime.datetime(2023, 5, 13, 12, 35, 31, 822756, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='novatarefa',
            name='data_inicio_planejado',
            field=models.DateField(default=datetime.datetime(2023, 5, 3, 12, 35, 31, 822756, tzinfo=utc)),
        ),
    ]
