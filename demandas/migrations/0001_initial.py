# Generated by Django 3.2.18 on 2023-04-06 19:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='StatusBacklog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NovaDemanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(max_length=255)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
                ('nome_solicitante', models.CharField(max_length=255, null=True)),
                ('retorno_financeiro', models.DecimalField(decimal_places=2, default=0, max_digits=50, validators=[django.core.validators.MinValueValidator(0)])),
                ('base_calculo_retorno', models.TextField(null=True)),
                ('retorno_qualitativo', models.TextField(null=True)),
                ('link_analise', models.URLField(blank=True, null=True)),
                ('observacao', models.TextField(null=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='demandas.categoria')),
                ('setor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='demandas.setor')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='demandas.statusbacklog')),
                ('usuario_criacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
