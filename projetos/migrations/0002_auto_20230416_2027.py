# Generated by Django 3.2.18 on 2023-04-16 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novoprojeto',
            name='fase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.faseprojeto'),
        ),
        migrations.AlterField(
            model_name='novoprojeto',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetos.statusprojeto'),
        ),
    ]
