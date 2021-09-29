from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Mobile
from .forms import MobileForm
# Create your views here.
def load_form(request):
    form=MobileForm
    return render(request,"form.html",{'form':form})

def add(request):
    form=MobileForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    mobile=Mobile.objects.all
    return render(request,'show.html',{'mobile':mobile})

def Project(request):    
    return render(request,"project.html")

def Access(request):    
    return render(request,"access.html")

def Camera(request):    
    return render(request,"camera.html")

def Color(request):    
    return render(request,"color.html")

def Home(request):    
    return render(request,"home.html")

def Phone(request):    
    return render(request,"phone.html")