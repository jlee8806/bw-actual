# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170113_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
