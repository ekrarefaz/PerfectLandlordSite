from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

from property.models import Property
from user.models import Profile

class PropertyInspection(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete = models.CASCADE)
    date_time = models.DateTimeField(default=datetime.now, blank=False)

class InspectionRegistration(models.Model):
    id = models.BigAutoField(primary_key=True)
    inspection = models.ForeignKey(PropertyInspection, on_delete = models.CASCADE)
    inspector = models.ForeignKey(User, on_delete = models.CASCADE)
    registered_on = models.DateTimeField(auto_now_add=True, blank=True)