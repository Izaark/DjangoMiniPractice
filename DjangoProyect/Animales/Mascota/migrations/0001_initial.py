# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-08 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('folio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
            },
        ),
    ]
