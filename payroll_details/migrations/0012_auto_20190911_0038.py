# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-09-10 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_details', '0011_auto_20190910_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_mname',
            field=models.CharField(default=None, max_length=250, verbose_name='Middle Name'),
        ),
    ]