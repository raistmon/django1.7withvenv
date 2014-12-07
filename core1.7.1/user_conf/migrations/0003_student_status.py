# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_conf', '0002_remove_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Status',
            field=models.BooleanField(default=True, verbose_name=b'Aktif'),
            preserve_default=True,
        ),
    ]
