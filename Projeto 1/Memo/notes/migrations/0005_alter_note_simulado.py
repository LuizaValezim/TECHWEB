# Generated by Django 3.2.7 on 2021-09-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20210929_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='simulado',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]