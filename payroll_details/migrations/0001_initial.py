# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-09-07 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_fname', models.CharField(max_length=250)),
                ('e_mname', models.CharField(max_length=250, null=True)),
                ('e_lname', models.CharField(max_length=250)),
                ('e_age', models.IntegerField()),
                ('e_phone', models.IntegerField()),
                ('e_email', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CTC_Year', models.IntegerField()),
                ('salary_month', models.CharField(max_length=15)),
                ('salary_year', models.IntegerField()),
                ('other_allowances', models.FloatField()),
                ('other_deductions', models.FloatField()),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll_details.Employee')),
            ],
        ),
    ]
