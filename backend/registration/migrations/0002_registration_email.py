# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]