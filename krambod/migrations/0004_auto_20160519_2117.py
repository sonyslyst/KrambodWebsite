# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 19:17
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krambod', '0003_auto_20160519_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informasjon',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
