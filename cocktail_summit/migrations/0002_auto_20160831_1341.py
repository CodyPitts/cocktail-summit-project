# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-31 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail_summit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
