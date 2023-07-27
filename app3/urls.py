app_name="thirdapp"

from django.urls import path
from app3.views import *

urlpatterns = [
    path("index3/",index3,name="index3"),
    path("new3/",new3,name="new3"),
    path("string3/",string3,name="string3")
]
