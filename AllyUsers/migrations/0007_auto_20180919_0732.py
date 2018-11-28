# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-19 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllyUsers', '0006_auto_20180915_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, b'Male'), (2, b'Feamle')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media/uploads'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
