# Generated by Django 3.0.2 on 2020-04-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nightcargoapp', '0012_auto_20200415_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='delivery_address',
            field=models.CharField(default='Boş Adres', max_length=100),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='delivery_minute',
            field=models.CharField(choices=[('0', '00'), ('1', '05'), ('2', '10'), ('3', '15'), ('4', '20'), ('5', '25'), ('6', '30'), ('7', '35'), ('8', '40'), ('9', '45'), ('10', '50'), ('11', '55'), ('12', '60')], default=25, max_length=6),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='sent_minute',
            field=models.CharField(choices=[('0', '00'), ('1', '05'), ('2', '10'), ('3', '15'), ('4', '20'), ('5', '25'), ('6', '30'), ('7', '35'), ('8', '40'), ('9', '45'), ('10', '50'), ('11', '55'), ('12', '60')], default=25, max_length=6),
        ),
    ]
