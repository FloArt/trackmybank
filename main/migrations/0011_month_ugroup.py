# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-06 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190106_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='month',
            name='ugroup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Group', verbose_name='user group'),
            preserve_default=False,
        ),
    ]