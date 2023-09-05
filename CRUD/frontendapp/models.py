from django.db import models

# Create your models here.
class signupDB(models.Model):
    Username = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    
    
    
    
class cartdb(models.Model):
    
    username=models.CharField(max_length=300,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
    tprice=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True,blank=True)
    
    
    
    
class checkoutDb(models.Model):
    district = models.CharField(max_length=100, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    adresstwo = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    zip = models.IntegerField(null=True)
    mobile = models.IntegerField(null=True)
    
    
    