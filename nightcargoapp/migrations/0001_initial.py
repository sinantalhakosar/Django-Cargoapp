# Generated by Django 3.0.2 on 2020-04-06 00:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('cargo_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ship_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('delivery_time', models.DateTimeField(help_text='Enter desired delivery time')),
                ('delivery_address', models.TextField(help_text='Enter desired delivery address', max_length=100)),
                ('status', models.CharField(choices=[('AC', 'Acceptance'), ('TR', 'Transfer'), ('DL', 'Delivery')], default='AC', max_length=2)),
                ('tracking_number', models.CharField(max_length=120, null=True)),
                ('weight', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(50)])),
                ('shipping_total', models.DecimalField(decimal_places=2, default=5.99, max_digits=100)),
                ('courier', models.ManyToManyField(related_name='courier', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ManyToManyField(related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ManyToManyField(related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('warehouse_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('warehouse_name', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=100)),
                ('couriers', models.ManyToManyField(related_name='couriers', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ManyToManyField(related_name='manager', to=settings.AUTH_USER_MODEL)),
                ('officers', models.ManyToManyField(related_name='officers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tck_no', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)])),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=150, null=True, unique=True)),
                ('address', models.TextField(max_length=100)),
                ('signup_confirmation', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CargoHistory',
            fields=[
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cargo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='nightcargoapp.Cargo')),
                ('courier_history', models.ManyToManyField(related_name='courier_history', to='nightcargoapp.Profile')),
                ('warehouse_history', models.ManyToManyField(related_name='warehouse_history', to='nightcargoapp.Warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='cargo',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse', to='nightcargoapp.Warehouse'),
        ),
    ]