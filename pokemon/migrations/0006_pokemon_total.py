# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-19 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0005_auto_20180519_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='total',
            field=models.IntegerField(blank=True, default=False),
        ),
    ]
