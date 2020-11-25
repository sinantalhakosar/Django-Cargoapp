from django.db import models
import uuid
from django.contrib.auth.models import User

from .address import Address


class Warehouse(models.Model):
    warehouse_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    warehouse_name = models.CharField(max_length=30)
    manager = models.ManyToManyField(User, blank=False, related_name='manager')
    couriers = models.ManyToManyField(User, blank=False, related_name='couriers')
    officers = models.ManyToManyField(User, blank=False, related_name='officers')
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
