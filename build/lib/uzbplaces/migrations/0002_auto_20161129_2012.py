# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 15:12
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uzbplaces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='location',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42, null=True, verbose_name="Location"),
        ),
        migrations.AddField(
            model_name='region',
            name='location',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42, null=True, verbose_name="Location"),
        ),
    ]