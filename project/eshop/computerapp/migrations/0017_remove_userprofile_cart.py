# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-05 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computerapp', '0016_auto_20171105_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='cart',
        ),
    ]
