from core.models import Example
from urllib import request
from django.shortcuts import render
def main (request): 
    if request.method =='POST':
        from_number = request.POST.get('first')
        to_number = request.POST.get('second')
        items = Example.objects.filter(cost__range=(from_number, to_number))
        return render(request,'main.html',{"items":items})
    else:
        items = Example.objects.all()
        return render(request,'main.html',{"items":items})


# Create your views here.
