from django.db import models

# Create your models here.
class UserRegistation(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    pNumber = models.IntegerField()
    password = models.CharField(max_length=150)