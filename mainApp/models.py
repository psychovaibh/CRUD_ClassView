from django.db import models



class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11,default="")
    dsg = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    city = models.CharField(max_length=20,default="",null=True,blank=True)
    state = models.CharField(max_length=20,default="",null=True,blank=True)