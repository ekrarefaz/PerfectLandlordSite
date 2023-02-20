from django.db import models

from django.contrib.auth.models import User

from landlord.models import Property, Profile

class PropertyInspection(models.Model):
    inspection_id = models.BigAutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete = models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True, blank=False)

class InspectionRegistration(models.Model):
    registration_id = models.BigAutoField(primary_key=True)
    inspection_id = models.ForeignKey(PropertyInspection, on_delete = models.CASCADE)
    inspector_id = models.ForeignKey(User, on_delete = models.CASCADE)
    registered_on = models.DateTimeField(auto_now_add=True, blank=True)