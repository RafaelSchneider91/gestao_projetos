# Generated by Django 3.2.18 on 2023-04-09 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demandas', '0004_alter_novademanda_setor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='novademanda',
            old_name='setor',
            new_name='setor_demanda',
        ),
    ]