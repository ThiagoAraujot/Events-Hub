from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    salary = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    client_name = models.CharField(max_length=200)
    guests = models.IntegerField(blank=True, null=True)
    employees = models.ManyToManyField(
        Employee, related_name='events', blank=True)
