# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('re_app', '0002_auto_20160701_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='show',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='station',
            name='position_x',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='position_y',
            field=models.FloatField(blank=True, null=True),
        ),
    ]