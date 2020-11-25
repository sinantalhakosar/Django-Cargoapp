from django.contrib.auth.models import User
from django.db import models
import uuid


class Address(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    header = models.CharField(max_length=20, blank=False, default="Address")
    description = models.TextField(max_length=100, blank=False)
    district = models.TextField(max_length=50, blank=False)
    city = models.TextField(max_length=50, blank=False)
    resident = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resident', null=True)
