# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-14 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventregistration_using_transportation'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_transportation',
            field=models.BooleanField(default=False, verbose_name='Rútur'),
        ),
    ]
