# Generated by Django 3.2.18 on 2023-05-03 12:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0007_auto_20230503_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novatarefa',
            name='data_fim_planejado',
            field=models.DateField(default=datetime.datetime(2023, 5, 13, 12, 42, 25, 305911, tzinfo=utc)),
        ),
    ]
