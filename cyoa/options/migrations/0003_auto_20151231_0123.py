# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0002_text_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(default='image url', max_length=40),
        ),
        migrations.AlterField(
            model_name='text',
            name='description',
            field=models.CharField(default='text', max_length=40),
        ),
    ]
