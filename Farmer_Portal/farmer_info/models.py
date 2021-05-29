from django.db import models

# Create your models here.

class farmer(models.Model):
    name = models.CharField(max_length=120)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField(max_length=120)
    photo = models.FileField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
