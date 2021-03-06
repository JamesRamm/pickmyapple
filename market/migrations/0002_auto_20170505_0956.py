# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-05 09:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0001_initial'),
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketitem',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='market_offers', to='plants.Plant'),
        ),
        migrations.AddField(
            model_name='marketitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='marketitem',
            name='wanted_plant',
            field=models.ForeignKey(blank=True, help_text='The plant desired in return for the offered crop', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='market_wanted', to='plants.Plant'),
        ),
    ]
