from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

from property.models import Property

class Identity(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.CharField(max_length=30, blank=False)
    # file = models.FileField(upload_to ='files/identity/', null=True, blank=False)

class Residential(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.CharField(max_length=30, blank=False)
    # file = models.FileField(upload_to ='files/residential/')

class Employment(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.CharField(max_length=30, blank=False)
    # file = models.FileField(upload_to ='files/income/')

class Income(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.CharField(max_length=30, blank=False)
    # file = models.FileField(upload_to ='files/income/')

class Application(models.Model):
    id = models.BigAutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete = models.CASCADE)
    tenant = models.ForeignKey(User, on_delete = models.CASCADE)
    date_time = models.DateTimeField(default=datetime.now, blank=False)
    cover_letter = models.TextField(max_length=500, blank=True)

class ApplicationIdentity(models.Model):
    id = models.BigAutoField(primary_key=True)
    application = models.ForeignKey(Application, on_delete = models.CASCADE)
    identity = models.ForeignKey(Identity, on_delete = models.CASCADE)

    class Meta:
        unique_together = (("application", "identity"),)
    
class ApplicationResidential(models.Model):
    id = models.BigAutoField(primary_key=True)
    application = models.ForeignKey(Application, on_delete = models.CASCADE)
    residential = models.ForeignKey(Residential, on_delete = models.CASCADE)

    class Meta:
        unique_together = (("application", "residential"),)

class ApplicationEmployment(models.Model):
    id = models.BigAutoField(primary_key=True)
    application = models.ForeignKey(Application, on_delete = models.CASCADE)
    employment = models.ForeignKey(Employment, on_delete = models.CASCADE)

    class Meta:
        unique_together = (("application", "employment"),)

class ApplicationIncome(models.Model):
    id = models.BigAutoField(primary_key=True)
    application = models.ForeignKey(Application, on_delete = models.CASCADE)
    income = models.ForeignKey(Income, on_delete = models.CASCADE)

    class Meta:
        unique_together = (("application", "income"),)