# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180414_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
    ]
