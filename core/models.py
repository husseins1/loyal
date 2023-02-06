from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Group(models.Model):
    type = models.CharField(max_length=50)

class costumer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    credit = models.CharField(max_length=50)
    identity = models.CharField(max_length=50)
    birthday = models.DateField()
    group = models.ForeignKey(Group,on_delete=models.CASCADE,null=True)

