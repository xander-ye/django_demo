# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-30 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170430_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='participator',
            field=models.ManyToManyField(blank=True, null=True, to='main.ParticipatorInfo', verbose_name='\u5df2\u62a5\u540d\u7528\u6237'),
        ),
    ]