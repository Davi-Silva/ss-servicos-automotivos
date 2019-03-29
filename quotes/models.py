from django.db import models
import datetime

# Create your models here.
class Quote(models.Model):
    fullname = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=13, blank=False, null=False)
    vehicle_model = models.CharField(max_length=120, blank=False)
    vehicle_location = models.CharField(max_length=30, blank=False)
    message = models.TextField()

    def __str__(self):
        return self.fullname.upper()
        