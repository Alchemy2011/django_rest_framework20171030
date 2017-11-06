# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pid', models.BigIntegerField()),
                ('cid', models.BigIntegerField()),
                ('avatar', models.CharField(blank=True, max_length=512)),
                ('username', models.CharField(blank=True, max_length=512)),
                ('created_at', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True)),
                ('like_counts', models.IntegerField(blank=True)),
                ('reply', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('cid', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('banner', models.CharField(max_length=256)),
                ('avatar', models.CharField(max_length=512)),
                ('verified', models.BooleanField(default=0)),
                ('name', models.CharField(max_length=128)),
                ('intro', models.TextField(blank=True)),
                ('like_counts', models.IntegerField(blank=True)),
                ('play_counts', models.IntegerField()),
                ('fans_counts', models.IntegerField()),
                ('follow_counts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Copyright',
            fields=[
                ('pcid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('pid', models.BigIntegerField()),
                ('cid', models.BigIntegerField()),
                ('roles', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('pid', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('preview', models.CharField(blank=True, max_length=512)),
                ('video', models.CharField(blank=True, max_length=512)),
                ('video_format', models.CharField(blank=True, max_length=512)),
                ('category', models.CharField(max_length=512)),
                ('created_at', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('play_counts', models.IntegerField()),
                ('like_counts', models.IntegerField()),
                ('thumbnail', models.CharField(blank=True, max_length=512)),
            ],
        ),
    ]