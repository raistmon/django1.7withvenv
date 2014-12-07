# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_conf', '0003_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Activation',
            field=models.CharField(max_length=200, unique=True, null=True, verbose_name=b'Aktivasyon Kodu', blank=True),
            preserve_default=True,
        ),
    ]
