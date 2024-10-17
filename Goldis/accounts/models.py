from django.db import models


class Account(models.Model):
    User_ID = models.BigAutoField(primary_key=True)  
    phone_number = models.CharField(max_length=14)
    address = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=128) 
    user_type = models.IntegerField(null=True, blank=True)  
    national_ID = models.CharField(max_length=10 , null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    rial_balance = models.CharField(max_length=10)
    gold_balance = models.CharField(max_length=10)