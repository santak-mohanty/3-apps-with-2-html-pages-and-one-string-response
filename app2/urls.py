app_name="secondapp"
from django.urls import path
from app2.views import *

urlpatterns = [
    path("index2/",index2,name="index2"),
    path("new2/",new2,name="new2"),
    path("string2/",string2,name="string2")
]
