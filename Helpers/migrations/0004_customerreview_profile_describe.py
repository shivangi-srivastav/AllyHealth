# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-20 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helpers', '0003_auto_20180920_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerreview',
            name='profile_describe',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
