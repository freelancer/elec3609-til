# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 02:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tilweb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posttag',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='posttag',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
