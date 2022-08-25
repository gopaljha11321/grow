from pyexpat import model
from django.db import models
class Contect(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=250)
    