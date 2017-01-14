from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django import forms
# Create your models here.

class rsvp(models.Model):
    Yes = 'Yes'
    No = 'No'
    attend_choices = (
        (Yes, 'Yes'),
        (No, 'No'),
        )
    name = models.CharField(max_length=30, default='Name')
    guest = models.CharField(max_length=30, default='Guest Name')
    email = models.EmailField(blank=True, default = 'Email')
    # attend = models.CharField(max_length=30)
    attend = models.CharField(max_length=3,
        choices = attend_choices,
        default=Yes,
        )
    message = models.CharField(max_length=100,blank=True, default='Send up a message')
