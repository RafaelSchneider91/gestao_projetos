# Generated by Django 4.2 on 2023-05-20 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0029_alter_novatarefa_data_fim_planejado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novatarefa',
            name='data_fim_planejado',
            field=models.DateField(default=datetime.datetime(2023, 5, 30, 18, 52, 2, 401340, tzinfo=datetime.timezone.utc)),
        ),
    ]
