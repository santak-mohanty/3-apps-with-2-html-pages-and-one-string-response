from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    return render(request,"index1.html")

def new1(request):
    return render(request,"new1.html")

def string1(request):
    return HttpResponse("<h1>This is string response of app1</h1>")
