from django.db import models
import datetime


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    #borthday = models.DateTimeField(default=datetime.date(year=1990,month=10,day=12))

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.BooleanField(default=False)
    #hstsdfu = models.ForeignKey(Student)
