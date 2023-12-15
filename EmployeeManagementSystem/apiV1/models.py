from django.db import models

# Create your models here.


class Employee2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    date = models.DateField()
    salary = models.IntegerField()
    region = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
