# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField(default=0)),
                ('patient_name', models.CharField(max_length=200)),
                ('measurement_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('sepsis_score', models.FloatField(default=0)),
                ('heart_rate', models.FloatField(default=0)),
                ('temperature', models.FloatField(default=0)),
                ('o2_saturation', models.FloatField(default=0)),
                ('blood_pressure', models.FloatField(default=0)),
                ('glasgow_coma_scale', models.FloatField(default=0)),
                ('respiratory_rate', models.FloatField(default=0)),
            ],
        ),
    ]
