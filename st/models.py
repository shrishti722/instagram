from datetime import datetime
from time import time
from django.db import models
DEPARTMENT_CHOICES = (
    ("HR", "HR"),
    ("SOFTWARE","SOFTWARE"),
    ("MARKETING","MARKETING"),
)
# Create your models here.
class employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    is_active = models.BooleanField() 
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    department = models.CharField(max_length=50,)

    choices= DEPARTMENT_CHOICES

    Image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    time = models.TimeField()
    date = models.DateField()
    datetime = models.DateTimeField()


def __str__(self):
    return self.emp_name

class student(models.Model):
    student_name = models.CharField(max_length=50)
    student_id = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False) 
    student_is = models.ForeignKey('student', on_delete= models.CASCADE, null=True)
    Image = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100, null=True)

class object(models.Model):
   Image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
   time = models.TimeField()
   date = models.DateField()
   datetime = models.DateTimeField()
   many = models.ManyToManyField('student')




















































