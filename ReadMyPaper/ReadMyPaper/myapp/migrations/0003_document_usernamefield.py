# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150419_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='userNameField',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
    ]
