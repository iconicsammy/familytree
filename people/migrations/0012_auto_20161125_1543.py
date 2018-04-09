# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20161125_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reference',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='verb',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
