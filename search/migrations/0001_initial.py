# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-25 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brand', models.IntegerField()),
                ('store', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('in_stock', models.BooleanField(choices=[('True', 'Yes'), ('False', 'No')], default='No')),
            ],
        ),
    ]
