# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-09-09 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_details', '0005_auto_20190909_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='e_id',
            field=models.IntegerField(default=0, verbose_name='Employee ID'),
            preserve_default=False,
        ),
    ]
