from django.contrib import admin
from . import models
# Register your models here.

myModels = [models.Warehouse, models.Cargo]  # iterable list
admin.site.register(myModels)
