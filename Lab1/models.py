from django.db import models

# Create your models here.

class prescription(models.Model):
    number = models.CharField(max_length = 4)
    firstname = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)
    content = models.CharField(max_length = 1000)
    VIP = models.BooleanField(default=False)