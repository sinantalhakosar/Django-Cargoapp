# Generated by Django 3.0.2 on 2020-04-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nightcargoapp', '0008_auto_20200410_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='receiver_gsm',
            field=models.CharField(default='00000000000', max_length=11),
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='receiver',
        ),
        migrations.AddField(
            model_name='cargo',
            name='receiver',
            field=models.CharField(default='John Doe', max_length=50),
        ),
    ]
