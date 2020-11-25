from django.db import models
import uuid
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .address import Address
from .warehouse import Warehouse
import os
import base64
from django.core.validators import MaxValueValidator, MinValueValidator


DAY_CHOICES = (
    ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
    ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'),
    ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'),
    ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'),
    ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')
)
MONTH_CHOICES = (
    ('1', 'OCAK'), ('2', 'ŞUBAT'), ('3', 'MART'), ('4', 'NİSAN'), ('5', 'MAYIS'),
    ('6', 'HAZİRAN'), ('7', 'TEMMUZ'), ('8', 'AĞUSTOS'), ('9', 'EYLÜL'), ('10', 'EKİM'),
    ('11', 'KASIM'), ('12', 'ARALIK')
)

HOUR_CHOICES = (
    ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
    ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'),
    ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'),
    ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24')
)

MINUTE_CHOICES = (
    ('0', '00'), ('1', '05'), ('2', '10'), ('3', '15'), ('4', '20'),
    ('5', '25'), ('6', '30'), ('7', '35'), ('8', '40'), ('9', '45'),
    ('10', '50'), ('11', '55'), ('12', '60')
)

DISTRICT_CHOICES = (
    ('0', 'TEPEBAŞI'), ('1', 'ODUNPAZARI'), ('2', 'SEYİTGAZİ')
)

class Cargo(models.Model):
    cargo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='sender')
    receiver = models.CharField(max_length=50, null=False, blank=False, default="John Doe")
    receiver_gsm = models.CharField(max_length=11, null=False, blank=False, default="00000000000")
    courier = models.ManyToManyField(User, related_name='courier')
    sender_address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    sent_day = models.CharField(max_length=6, choices=DAY_CHOICES, default=now().day)
    sent_month = models.CharField(max_length=6, choices=MONTH_CHOICES, default=now().month)
    sent_hour = models.CharField(max_length=6, choices=HOUR_CHOICES, default=now().hour)
    sent_minute = models.CharField(max_length=6, choices=MINUTE_CHOICES, default=now().minute)

    delivery_day = models.CharField(max_length=6, choices=DAY_CHOICES, default=now().day)
    delivery_month = models.CharField(max_length=6, choices=MONTH_CHOICES, default=now().month)
    delivery_hour = models.CharField(max_length=6, choices=HOUR_CHOICES, default=now().hour)
    delivery_minute = models.CharField(max_length=6, choices=MINUTE_CHOICES, default=now().minute)

    delivery_description = models.TextField(max_length=100, null=False, blank=False, default="Boş Adres")
    delivery_district = models.TextField(max_length=6, choices=DISTRICT_CHOICES, null=True, default=0)
    delivery_city = models.CharField(max_length=10, default="Eskişehir")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True, related_name='warehouse')

    class CargoStatus(models.TextChoices):
        ACCEPTANCE = 'AC', _('Acceptance')
        TRANSFER = 'TR', _('Transfer')
        DELIVERY = 'DL', _('Delivery')

    status = models.CharField(max_length=2, choices=CargoStatus.choices, default=CargoStatus.ACCEPTANCE)
    tracking_number = models.CharField(max_length=120, null=True)
    weight = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(50)], null=True)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)

