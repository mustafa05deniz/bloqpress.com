# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0003_sozler'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gelen_yazilar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gonderen_adi', models.CharField(max_length=30)),
                ('text', models.TextField(max_length=100000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
