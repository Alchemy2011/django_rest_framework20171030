# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-25 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerapp', '0008_auto_20171025_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cart',
            field=models.TextField(default='{}'),
        ),
    ]
