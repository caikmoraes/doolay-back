# Generated by Django 3.2.7 on 2021-11-23 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20211008_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='name',
            field=models.CharField(blank=True, default='none informed', max_length=256, null=True),
        ),
    ]