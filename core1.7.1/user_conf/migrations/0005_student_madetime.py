# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_conf', '0004_student_activation'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='MadeTime',
            field=models.DateTimeField(null=True, verbose_name=b'Olu\xc5\x9fturulma Tarihi', blank=True),
            preserve_default=True,
        ),
    ]
