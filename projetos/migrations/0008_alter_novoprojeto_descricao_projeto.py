# Generated by Django 4.2 on 2023-04-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0007_novoprojeto_descricao_projeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novoprojeto',
            name='descricao_projeto',
            field=models.TextField(),
        ),
    ]