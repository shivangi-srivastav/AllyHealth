# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-14 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesForce', '0004_checkingsalesforcecontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkingsalesforcecontact',
            name='birthdate_r',
            field=models.DateField(blank=True, null=True),
        ),
    ]
