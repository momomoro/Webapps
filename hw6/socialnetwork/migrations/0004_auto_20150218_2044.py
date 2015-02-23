# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0003_blogger'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='picture',
            field=models.FileField(upload_to=b'pictures', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='socialnetwork.Blogger'),
            preserve_default=True,
        ),
    ]
