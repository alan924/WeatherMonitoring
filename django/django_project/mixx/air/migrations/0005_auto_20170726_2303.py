# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0004_auto_20170718_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='imgurl',
            new_name='url',
        ),
        migrations.AddField(
            model_name='city',
            name='intro',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
