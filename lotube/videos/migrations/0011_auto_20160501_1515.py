# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-01 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_auto_20160417_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytic',
            name='video',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='analytic', serialize=False, to='videos.Video'),
        ),
    ]