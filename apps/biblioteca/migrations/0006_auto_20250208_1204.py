# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2025-02-08 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_auto_20250204_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, default='defaul.png', upload_to='portada'),
        ),
    ]
