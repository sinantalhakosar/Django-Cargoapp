from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .address import Address


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tck_no = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    first_name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=150, blank=False, unique=True, null=True)
    address = models.ManyToManyField(Address, blank=False, related_name='address')
    signup_confirmation = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
