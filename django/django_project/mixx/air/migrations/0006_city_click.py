# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0005_auto_20170726_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='click',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
