from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=200,default='')
    password=models.TextField()
    email=models.EmailField()
    Phonenum=models.IntegerField()
    Gender=models.TextField(default='')
    status=models.IntegerField(default=0)