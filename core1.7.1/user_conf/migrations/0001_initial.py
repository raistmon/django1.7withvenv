# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BirthDate', models.DateField(null=True, verbose_name=b'Do\xc4\x9fum Tarihi', blank=True)),
                ('Sex', models.CharField(default=b'Kad\xc4\xb1n', choices=[(b'Erkek', 'Erkek'), ('Kad\u0131n', 'Kad\u0131n')], max_length=200, blank=True, null=True, verbose_name='Cinsiyet')),
                ('Status', models.BooleanField(default=True, verbose_name=b'Aktif')),
                ('Grup', models.ForeignKey(verbose_name=b'Yetki', to='auth.Group')),
                ('Kullanici', models.ForeignKey(verbose_name=b'Kullan\xc4\xb1c\xc4\xb1 Ad\xc4\xb1', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['Kullanici'],
                'verbose_name': '\xd6\u011frenci Profili',
                'verbose_name_plural': '\xd6\u011frenci Profilleri',
            },
            bases=(models.Model,),
        ),
    ]
