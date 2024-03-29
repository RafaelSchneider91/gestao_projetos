# Generated by Django 3.2.18 on 2023-05-03 13:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0014_auto_20230503_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novatarefa',
            name='data_fim_planejado',
            field=models.DateField(default=datetime.datetime(2023, 5, 13, 13, 25, 22, 488453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='novatarefa',
            name='status_tarefa',
            field=models.CharField(choices=[('N', 'Não Iniciado'), ('E', 'Em andamento'), ('P', 'Pendente'), ('C', 'Concluido')], max_length=50),
        ),
    ]
