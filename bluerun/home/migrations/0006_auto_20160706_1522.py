# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 09:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160706_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 7, 6, 9, 52, 33, 500771, tzinfo=utc)),
        ),
    ]