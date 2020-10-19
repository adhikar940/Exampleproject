from django.db import models
from datetime import datetime, date

# Create your models here.


class FacultyProfile(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    #phone = models.CharField(max_length=300)
    Address = models.TextField(max_length=100)

    def __str__(self):
        return self.First_Name
