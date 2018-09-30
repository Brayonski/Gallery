# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='DEFAULT IMAGE', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]