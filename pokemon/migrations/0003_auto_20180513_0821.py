# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-13 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20180513_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='gen',
            field=models.IntegerField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type1',
            field=models.CharField(blank=True, default=False, max_length=120),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(blank=True, default=False, max_length=120),
        ),
    ]
