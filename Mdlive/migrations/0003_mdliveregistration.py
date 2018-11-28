# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-01 10:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Mdlive', '0002_auto_20181001_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='MdliveRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_patient_id', models.CharField(blank=True, max_length=255, null=True)),
                ('m_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('m_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('m_middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('m_username', models.CharField(blank=True, max_length=255, null=True)),
                ('m_address1', models.CharField(blank=True, max_length=255, null=True)),
                ('m_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('m_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('m_work_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('m_affiliation_id', models.CharField(blank=True, max_length=255, null=True)),
                ('m_jwt_token', models.CharField(blank=True, max_length=255, null=True)),
                ('m_istoken', models.BooleanField(default=False)),
                ('m_token1', models.CharField(blank=True, max_length=255, null=True)),
                ('m_token2', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mdlive_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
