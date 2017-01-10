# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 04:07
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations, models
import lights.models


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='color',
            field=colorful.fields.RGBColorField(colors=['#FFFFFF', '#FF0000', '#00FF00', '#0000FF', '#000000']),
        ),
        migrations.AlterField(
            model_name='light',
            name='position',
            field=models.IntegerField(unique=True, validators=[lights.models.position_validator]),
        ),
    ]