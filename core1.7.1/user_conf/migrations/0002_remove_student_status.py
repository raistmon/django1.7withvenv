# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_conf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Status',
        ),
    ]
