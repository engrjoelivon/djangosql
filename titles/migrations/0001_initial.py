# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Numeric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.CharField(unique=True, max_length=50)),
                ('number', models.SmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
    ]
