from django.db import models
from django.utils import timezone
from django import forms



# Create your models here.
class IncidentReport(models.Model):
    Location=models.CharField(max_length=1000)
    Incident_Department=models.CharField(max_length=1000)
    Date_Of_Incident=models.DateField(default=timezone.now)
    Time_Of_Incident=models.TimeField()
    Incident_Location=models.CharField(max_length=1000)
    Suspected_Cause=models.CharField(max_length=1000)
    Immediate_Action=models.CharField(max_length=1000)
    Environmental_Incident=models.CharField(max_length=1000)
    Injury_Illness=models.CharField(max_length=1000)
    Property_Damage=models.CharField(max_length=1000)
    Vehicle=models.CharField(max_length=1000)
    Reported_By=models.CharField(max_length=1000)

class MarkyticsUser(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

