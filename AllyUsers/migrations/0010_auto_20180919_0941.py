# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-19 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllyUsers', '0009_auto_20180919_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[(b'M', b'Male'), (b'F', b'Feamle')], max_length=2, null=True),
        ),
    ]
