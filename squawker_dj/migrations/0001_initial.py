# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 02:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squawk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]