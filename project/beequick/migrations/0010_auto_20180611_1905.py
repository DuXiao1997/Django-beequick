# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-11 11:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beequick', '0009_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ordered',
            new_name='orderid',
        ),
    ]
