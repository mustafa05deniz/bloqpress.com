# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0004_gelen_yazilar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('short_text', redactor.fields.RedactorField(verbose_name='Text')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
