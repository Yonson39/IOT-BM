# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-25 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20180825_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='CUSTOMER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u5ba2\u6237\u540d\u79f0')),
                ('phone', models.CharField(max_length=32, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('level', models.IntegerField(blank=True, choices=[(0, '\u666e\u901a'), (1, '\u7b49\u7ea71'), (2, '\u7b49\u7ea72'), (3, '\u7b49\u7ea73'), (4, '\u7b49\u7ea74'), (5, '\u7b49\u7ea75')], default=0, verbose_name='\u5ba2\u6237\u7b49\u7ea7')),
                ('creat_date', models.DateTimeField(verbose_name='\u5ba2\u6237\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237',
                'verbose_name_plural': '\u5ba2\u6237',
            },
        ),
        migrations.CreateModel(
            name='STORE',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('41474b63-a869-11e8-ab48-c4b3018f55c6'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='\u95e8\u5e97\u540d\u79f0')),
                ('bandwidth', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u95e8\u5e97\u5e26\u5bbd')),
                ('phone', models.CharField(max_length=32, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('linkman', models.CharField(max_length=32, null=True, verbose_name='\u8054\u7cfb\u4eba')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u95e8\u5e97\u5730\u5740')),
                ('create_time', models.DateField(auto_now=True)),
                ('type', models.IntegerField(blank=True, choices=[(0, '\u52a0\u76df'), (1, '\u76f4\u8425')], max_length=32, null=True, verbose_name='\u95e8\u5e97\u7c7b\u578b')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('customerid', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='asset.CUSTOMER', verbose_name='\u6240\u5c5e\u5ba2\u6237')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u95e8\u5e97',
                'verbose_name_plural': '\u5ba2\u6237\u95e8\u5e97',
            },
        ),
        migrations.AlterField(
            model_name='dev',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('4148cb91-a869-11e8-9349-c4b3018f55c6'), editable=False, primary_key=True, serialize=False),
        ),
    ]
