from django.db import models
import datetime


# 自定义查询对象
class StudentManager(models.manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    # borthday = models.DateTimeField(default=datetime.date(year=1990,month=10,day=12))

    # 自定义表名
    class Meta:
        db_table = 'custom_table'

    students1 = models.Manager()
    students2 = StudentManager()


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.BooleanField(default=False)
    #hstsdfu = models.ForeignKey(Student)
