# Generated by Django 3.0.2 on 2020-04-09 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nightcargoapp', '0005_address_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='type',
        ),
    ]