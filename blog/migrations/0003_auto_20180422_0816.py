# Generated by Django 2.0.2 on 2018-04-22 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180422_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 22, 8, 16, 29, 946668)),
        ),
    ]