from django.db import models

# Create your models here.
class location(models.Model):
    locationname=models.CharField(max_length=200)
    locationimage=models.ImageField()
class Eturf(models.Model):
    turfname=models.CharField(max_length=200)
    turfimage=models.ImageField()
    BookingPackage=models.TextField()
    Facilities=models.TextField()
    Time=models.TextField()
    manager=models.TextField(default='')
    locationname=models.TextField(default='')