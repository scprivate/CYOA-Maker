# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_ref', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='options.Text'),
        ),
    ]
