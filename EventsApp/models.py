# Defining Event model
from django.db import models
from django.conf import settings

class Event(models.Model):
    name = models.TextField(blank=True)
    url = models.URLField()