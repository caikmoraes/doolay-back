# Generated by Django 3.2.7 on 2021-11-23 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saude', '0002_auto_20211123_0800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estadosintomaitem',
            old_name='nome_sintoma',
            new_name='sintoma',
        ),
    ]
