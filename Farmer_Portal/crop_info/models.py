from django.db import models

# Create your models here.

class crop(models.Model):
    name = models.CharField(max_length=120)
    owner = models.CharField(max_length=120)
    contact = models.CharField(max_length=120)
    description  = models.CharField(max_length=250)
    prize = models.PositiveBigIntegerField()
    stock = models.PositiveIntegerField()
    photo = models.FileField()
