from django.db import models

# Create your models here.


class Department2(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role2(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    date = models.DateField()
    salary = models.IntegerField()
    region = models.CharField(max_length=50)
    # company = models.CharField(max_length=100)
    
    # Primary Keys Defining
    dept = models.ForeignKey(Department2, on_delete=models.CASCADE)
    role = models.ForeignKey(Role2, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
