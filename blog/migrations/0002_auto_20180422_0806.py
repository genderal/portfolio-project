# Generated by Django 2.0.2 on 2018-04-22 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 22, 8, 6, 39, 291258)),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]