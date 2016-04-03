# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20160326_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
