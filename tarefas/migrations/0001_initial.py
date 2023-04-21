# Generated by Django 4.2 on 2023-04-20 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projetos', '0006_alter_novoprojeto_nome_projeto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NovaTarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(max_length=255)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_inicio', models.DateTimeField()),
                ('data_fim_planejado', models.DateTimeField()),
                ('data_fim_realizado', models.DateTimeField(default=django.utils.timezone.now)),
                ('membros', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.novoprojeto')),
            ],
        ),
    ]
