from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index3(request):
    return render(request,"index3.html")

def new3(request):
    return render(request,"new3.html")

def string3(request):
    return HttpResponse("<h1>This is string response of app3</h1")