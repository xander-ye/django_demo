# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-29 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170429_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='regions',
        ),
        migrations.AddField(
            model_name='profile',
            name='regions',
            field=models.CharField(blank=True, choices=[('qingyang', '\u9752\u7f8a'), ('jinniu', '\u91d1\u725b'), ('wuhou', '\u6b66\u4faf'), ('chenghua', '\u6210\u534e'), ('gaoxing', '\u9ad8\u65b0\u533a'), ('gaoxingxiqu', '\u9ad8\u65b0\u897f\u533a'), ('wenjaing', '\u6e29\u6c5f'), ('shuangliu', '\u53cc\u6d41'), ('longqianyi', '\u9f99\u6cc9\u9a7f'), ('xindu', '\u65b0\u90fd'), ('pixian', '\u90eb\u53bf'), ('dujiangyan', '\u90fd\u6c5f\u5830'), ('qingbaijiang', '\u9752\u767d\u6c5f'), ('pengzhou', '\u5f6d\u5dde'), ('pujiang', '\u6d66\u6c5f'), ('dayi', '\u5927\u9091'), ('xinjin', '\u65b0\u6d25'), ('zongzhou', '\u5d07\u5dde'), ('qonglai', '\u909b\u5d03'), ('jintang', '\u91d1\u5802')], max_length=10, verbose_name='\u610f\u5411\u533a\u57df'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='styles',
        ),
        migrations.AddField(
            model_name='profile',
            name='styles',
            field=models.CharField(blank=True, choices=[('one', '\u666e\u901a\u4f4f\u5b85'), ('two', '\u82b1\u56ed\u6d0b\u623f'), ('three', '\u522b\u5885'), ('four', '\u5546\u94fa'), ('five', '\u5199\u5b57\u697c'), ('six', '\u516c\u5bd3\uff09')], max_length=10, verbose_name='\u610f\u5411\u7c7b\u578b'),
        ),
        migrations.DeleteModel(
            name='LikeRegion',
        ),
        migrations.DeleteModel(
            name='LikeStyle',
        ),
    ]
