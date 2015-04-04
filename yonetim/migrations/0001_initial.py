# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('resim', models.ImageField(upload_to=b'tmp/')),
                ('zaman', models.DateTimeField(null=True)),
                ('short_text', redactor.fields.RedactorField(verbose_name='Text')),
                ('Katagory', models.ForeignKey(to='yonetim.catagory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sayi_ismi', models.CharField(max_length=100)),
                ('sayi', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='raporlar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resim_Katalogu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resim1', models.ImageField(upload_to=b'tmp/')),
                ('resim2', models.ImageField(upload_to=b'tmp/')),
                ('resim3', models.ImageField(upload_to=b'tmp/')),
                ('resim4', models.ImageField(upload_to=b'tmp/')),
                ('resim5', models.ImageField(upload_to=b'tmp/')),
                ('resim6', models.ImageField(upload_to=b'tmp/')),
                ('resim7', models.ImageField(upload_to=b'tmp/')),
                ('resim8', models.ImageField(upload_to=b'tmp/')),
                ('resim9', models.ImageField(upload_to=b'tmp/')),
                ('resim10', models.ImageField(upload_to=b'tmp/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
