from pyexpat import model
from django import forms
from .models import *

class studentupdateform(forms.ModelForm):
    class Meta:
        model = student
        fields= ('student_name' , )