from django.db import models
from django.utils.timezone import now
import uuid
from .warehouse import Warehouse
from .profile import Profile
from .cargo import Cargo


class CargoHistory(models.Model):
    history_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    update_time = models.DateTimeField(default=now, editable=False, null=False, blank=False)
    warehouse_history = models.ManyToManyField(Warehouse, blank=False, related_name='warehouse_history')
    courier_history = models.ManyToManyField(Profile, blank=False, related_name='courier_history')
    cargo = models.OneToOneField(Cargo, on_delete=models.CASCADE)