# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='classNumField',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='dueDateField',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='document',
            name='promptField',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AddField(
            model_name='document',
            name='titleField',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
