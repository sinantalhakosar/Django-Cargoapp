# Generated by Django 3.0.2 on 2020-04-09 21:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nightcargoapp', '0002_auto_20200409_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='header',
            field=models.CharField(default='Address', max_length=20),
        ),
        migrations.AddField(
            model_name='address',
            name='resident',
            field=models.ManyToManyField(related_name='resident', to=settings.AUTH_USER_MODEL),
        ),
    ]
