# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AddField(
            model_name='post',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 2, 14, 33, 329000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 2, 14, 41, 136000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
