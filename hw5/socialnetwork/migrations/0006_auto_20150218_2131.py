# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialnetwork', '0005_auto_20150218_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('picture', models.FileField(upload_to=b'pictures', blank=True)),
                ('following', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='following',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
