# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='description',
            field=models.CharField(default='memes', max_length=40),
        ),
    ]