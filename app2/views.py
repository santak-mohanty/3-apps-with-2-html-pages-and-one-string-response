from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index2(request):
    return render(request,"index2.html")

def new2(request):
    return render(request,"new2.html")

def string2(request):
    return HttpResponse("<h1>This is string response of app2</h1>")