# Generated by Django 4.2 on 2023-05-07 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0020_alter_novoprojeto_options_emails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emails',
            old_name='vaga',
            new_name='projeto',
        ),
    ]
