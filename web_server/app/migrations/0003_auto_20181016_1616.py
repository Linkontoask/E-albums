# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-16 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181015_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='type',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='point',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='picture',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
