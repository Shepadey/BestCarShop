
from core.forms import ExampleForm
from core.models import Example
from urllib import request
from django.shortcuts import redirect, render
def main (request): 
    if request.method =='POST':
        from_number = request.POST.get('first')
        to_number = request.POST.get('second')
        items = Example.objects.filter(cost__range=(from_number, to_number))
        return render(request,'main.html',{"items":items})
    else:
        items = Example.objects.all()
        return render(request,'main.html',{"items":items})
def form(request):
    forms =ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request,'add.html',{'forms':forms})
    


# Create your views here.
