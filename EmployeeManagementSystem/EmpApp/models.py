from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    # Foreign Keys
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.IntegerField(default=0)
