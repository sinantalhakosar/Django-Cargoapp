# Generated by Django 3.0.2 on 2020-04-14 20:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nightcargoapp', '0010_auto_20200412_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='time_sent',
        ),
        migrations.AddField(
            model_name='cargo',
            name='date_sent',
            field=models.DateField(default=datetime.datetime(2020, 4, 14, 20, 38, 38, 183639, tzinfo=utc)),
        ),
    ]
