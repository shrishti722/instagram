
from django import template
from django.shortcuts import redirect, render

from aaa.settings import LOGIN_REDIRECT_URL, LOGIN_URL
from .forms import *
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.



def index(request):
    filter = student.objects.filter(student_name="shrishti")
    print('shrishti', filter)
    # get= student.objects.get(roll_no= 7)
    # create=student.objects.create(student_name= 'pie')
    stu = student.objects.all(student_name="pie")
    print(stu)

    return render(request, 'index.html')


def form(request):
    Firstname = request.POST.get('firstname')
    Lastname = request.POST.get('lastname')
    print("as", Firstname, Lastname)
    return render(request, 'form.html')


def table(request):
    stu = student.objects.all()
    context = {
        "student": stu
    }
    return render(request, 'table.html', context)


def edit(request, id):
    stu = student.objects.get(id=id)
    return render(request, 'edit.html', {'student': stu})


def update(request, id):
    stu = student.objects.get(id=id)
    var = request.POST.get("name")
    print(var)
    form = studentupdateform(request.POST, instance=stu)
    if form.is_valid():
        form.save()
        return redirect("table")

    context = {
        'student' : stu,
    }
    return render(request, 'edit.html', context)

class Adminlogin(LoginView):
    print("Shrishti login")
    template_name = "Login.html"

    @login_required
    def side_bar(request):
        return render(request, 'side_login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})        
    

def socials(request):
