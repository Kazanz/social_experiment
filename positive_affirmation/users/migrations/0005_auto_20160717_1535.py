# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 20:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_affirmation_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encouragement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='affirmation',
            name='likes',
        ),
        migrations.AddField(
            model_name='encouragement',
            name='affirmation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Affirmation'),
        ),
        migrations.AddField(
            model_name='encouragement',
            name='encourager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
