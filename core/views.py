from urllib import request
from django.shortcuts import render
def main (request): 
    names = ["Alexandr","Vasiliy","Pavel","Andrey","Dmitriy"]
    return render(request,'main.html',{"names":names})



# Create your views here.
