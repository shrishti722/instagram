
from turtle import st, update
from django.forms import Form
from django.urls import path
from .views import *



urlpatterns = [
    path('index/',index, name= 'index'),
    path('form/',form, name= 'form'),
    path('table/',table, name= 'table'),
    path('table/edit/<int:id>', edit, name='edit'),
    path('update/<int:id>',update, name="update")
    
]

