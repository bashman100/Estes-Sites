# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dynamics', '0002_auto_20161117_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='date_made',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]