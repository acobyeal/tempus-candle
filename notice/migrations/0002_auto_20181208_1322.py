# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-08 04:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NoticePost',
            new_name='Notice',
        ),
    ]
