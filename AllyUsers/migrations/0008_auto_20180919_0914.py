# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-19 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllyUsers', '0007_auto_20180919_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'media/uploads'),
        ),
    ]
