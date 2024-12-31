from django.db import models
from Admin.models import*
# Create your models here.
class Userreg(models.Model):
    username=models.TextField()
    password=models.CharField(max_length=200)
    email=models.EmailField()
    Phonenum=models.IntegerField()
    status=models.IntegerField(default=0)
class contact(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField()
    text=models.TextField()
class booking(models.Model):
    username=models.ForeignKey(Userreg,on_delete=models.CASCADE)
    turfname=models.ForeignKey(Eturf,on_delete=models.CASCADE)
    Email=models.TextField(default='')
    Date=models.TextField()
    Time=models.TextField()
    status=models.IntegerField(default=0)

    