from core.models import Example
from urllib import request
from django.shortcuts import render
def main (request): 
    items = Example.objects.all()
    return render(request,'main.html',{"items":items})



# Create your views here.
