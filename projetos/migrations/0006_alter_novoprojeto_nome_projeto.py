# Generated by Django 3.2.18 on 2023-04-17 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demandas', '0011_auto_20230416_2019'),
        ('projetos', '0005_auto_20230417_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novoprojeto',
            name='nome_projeto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demandas.novademanda'),
        ),
    ]
