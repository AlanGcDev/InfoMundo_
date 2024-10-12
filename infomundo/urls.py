from django.urls import path
from .views.index import *


urlpatterns = [
    path("", home,  name="index")  
]
