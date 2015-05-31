# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rant', '0006_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='clip',
            field=models.ForeignKey(blank=True, to='rant.Clip', null=True),
            preserve_default=True,
        ),
    ]
