# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0002_auto_20171202_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='parent_id',
            new_name='parent',
        ),
    ]
