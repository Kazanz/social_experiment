# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 20:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_affirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='affirmation',
            name='created',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 17, 20, 22, 22, 233645, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
