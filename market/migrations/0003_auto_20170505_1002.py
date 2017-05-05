# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-05 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20170505_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketitem',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='marketitem',
            name='quantity_units',
            field=models.IntegerField(choices=[(1, 'Individual plants'), (2, 'Kilograms')], help_text='Quantity units for plant offered for trade'),
        ),
    ]