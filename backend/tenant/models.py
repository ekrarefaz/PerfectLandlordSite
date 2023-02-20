from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

from landlord.models import Property

class SavedProperty(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete = models.CASCADE)
    tenant = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        unique_together = (("property", "tenant"),)