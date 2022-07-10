from email.headerregistry import Address
from django.db import models

class Student(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    number=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    course=models.CharField(max_length=50)
    password=models.CharField(max_length=50)