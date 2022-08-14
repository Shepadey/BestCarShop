
from django.http import JsonResponse
from core.forms import ExampleForm
from core.models import Example
from urllib import request
from django.shortcuts import redirect, render
from django.db.models import  Max, Min
def main (request): 
    if request.method =='POST':
        if request.is_valid():
            from_number = request.POST.get('first')
            to_number = request.POST.get('second')
            items = Example.objects.filter(cost__range=(from_number, to_number))
            return render(request,'main.html',{"items":items})
    else:
        items = Example.objects.all()
        min_cost = Example.objects.all().aggregate(Min('cost'))
        max_cost = Example.objects.all().aggregate(Max('cost'))
        return render(request,'main.html',{"items":items,"min_cost":min_cost,"max_cost":max_cost})
def form(request):
    forms =ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request,'add.html',{'forms':forms})
def get_items(request):
    return JsonResponse({'info':'Фильтр работает'})

def search_items(request):
    print(request.GET)
    return JsonResponse({'info':'Поиск работает'})


    


# Create your views here.
