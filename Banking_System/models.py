from datetime import datetime, timezone
from os import name
from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    balance = models.IntegerField()

class TransactionHistory(models.Model):
    senderName=models.CharField(max_length=30)
    receiverName=models.CharField(max_length=30)
    amount=models.IntegerField()
    timings=models.DateTimeField(default=datetime.now,blank=True)