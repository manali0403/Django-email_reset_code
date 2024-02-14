from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mark = models.FloatField()
    add = models.CharField(max_length=20)

    