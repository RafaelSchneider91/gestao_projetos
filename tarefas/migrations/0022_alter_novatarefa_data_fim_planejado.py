# Generated by Django 4.2 on 2023-05-07 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0021_auto_20230505_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novatarefa',
            name='data_fim_planejado',
            field=models.DateField(default=datetime.datetime(2023, 5, 17, 14, 6, 22, 214204, tzinfo=datetime.timezone.utc)),
        ),
    ]
