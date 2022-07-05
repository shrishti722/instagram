from datetime import datetime
from email.policy import default
from time import time
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField 
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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, relatd_name='followers')
    following = models.ManyToManyField(User, related_name='following')
    profile_picture = models.ImageField(upload_to='uploads/profile_pictures/', default='uploads/profile_pictures/default.png', blank=True)
    
class POST(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE related_names= 'user')
    image = models.ImageField(upload_to='uploads/image/', blank=True)
    likes = models.ManyToManyField(User, related_name='user') 
    profile = models.ForeignKey(User, on_delete=models.CASCADE related_name= 'user')

class Reels(models.Model):
    reels = models.FileField(upload_to='uploads/reels/', blank=True)
    likes = models.ManyToManyField(User, related_name='user')

class Story(models.Model):
    story = models.ImageField(upload_to='uploads/story', blank=True)
    profile = models.ForeignKey(User, on_delete= models.CASCAD related_name='profile_table')