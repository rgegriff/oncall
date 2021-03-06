# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 00:46
from __future__ import unicode_literals

import colorful.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(unique=True)),
                ('color', colorful.fields.RGBColorField()),
                ('assigned_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
