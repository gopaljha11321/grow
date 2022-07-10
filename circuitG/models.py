from email.headerregistry import Address
from django.db import models
class User(models.Model):
    email=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    otp=models.IntegerField()
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    number=models.CharField(max_length=15)