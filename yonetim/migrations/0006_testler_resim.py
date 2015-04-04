# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0005_testler'),
    ]

    operations = [
        migrations.AddField(
            model_name='testler',
            name='resim',
            field=models.ImageField(default=1, upload_to=b'tmp/'),
            preserve_default=False,
        ),
    ]
