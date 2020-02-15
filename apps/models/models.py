from django.db import models
import datetime
from django.utils import timezone


# 自定义查询对象
class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    borthday = models.DateTimeField(default=datetime.datetime.now())

    # 自定义表名
    class Meta:
        db_table = 'custom_table'

    students1 = models.Manager()
    students2 = StudentManager()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.BooleanField(default=False)
    students = models.ForeignKey(Student, default=None, on_delete=models.SET_DEFAULT)

