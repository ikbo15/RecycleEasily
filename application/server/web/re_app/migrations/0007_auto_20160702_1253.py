# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('re_app', '0006_auto_20160702_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reg_date',
            field=models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438'),
        ),
    ]