# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-09-09 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_details', '0007_salary_leave_month_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='emp',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='leave_month_year',
        ),
        migrations.AddField(
            model_name='salary',
            name='no_of_days',
            field=models.IntegerField(default=0, verbose_name='No. of working days'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salary',
            name='no_of_days_worked',
            field=models.IntegerField(default=0, verbose_name='No. of days worked'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Leave',
        ),
    ]
