from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=13, blank=False, null=False)
    subject = models.CharField(max_length=120, blank=False, null=False)
    message = models.TextField()

    def __str__(self):
        return self.name.upper()