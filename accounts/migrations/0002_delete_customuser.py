# Generated by Django 4.1.5 on 2023-01-28 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="CustomUser",),
    ]
