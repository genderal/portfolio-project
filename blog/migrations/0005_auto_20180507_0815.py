# Generated by Django 2.0.2 on 2018-05-07 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180422_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 7, 8, 15, 11, 900426)),
        ),
    ]