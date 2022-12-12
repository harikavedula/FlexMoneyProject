from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
class User(models.Model):

    name=models.TextField()
    userid=models.IntegerField()
    email=models.TextField()
    phno=models.TextField()
    age=models.IntegerField()
    password=models.TextField()

class Reservations(models.Model):

    resid=models.IntegerField()
    userid=models.IntegerField()
    payamount=models.IntegerField()
    batch=models.TextField()
    month=models.TextField()
    year=models.TextField()
