from django.db import models

# Create your models here.
class user(models.Model):
    uname=models.CharField(max_length=20)
    passw=models.CharField(max_length=20)
    email=models.CharField(max_length=50,default=1)