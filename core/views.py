
from django.http import JsonResponse
from core.forms import ExampleForm
from core.models import Example
from urllib import request
from django.shortcuts import redirect, render
from django.db.models import  Max, Min
def create_dict_with_items(items):
    response = {}
    for item in items:
        response[item.id] = {
            'id' : item.id,
            'name' : item.name,
            'color' : item.color,
            'cost' : item.cost,
            'image' : item.image.url
        }
    return response
def main (request): 
    '''if request.method =='get':
        from_number = request.GET.get('first')
        to_number = request.GET.get('second')
        items = Example.objects.filter(cost__range=(0, 20000))
        return render(request,'main.html',{"items":items})'''

    items = Example.objects.all()
    min_cost = Example.objects.all().aggregate(Min('cost'))
    max_cost = Example.objects.all().aggregate(Max('cost'))
    from_number = request.GET.get('first')
    to_number = request.GET.get('second')
    if (from_number !=None or to_number !=None) and (from_number != '' or to_number !=''):
        items = Example.objects.filter(cost__range=(from_number, to_number))
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
    from_number = request.GET.get('from')
    to_number = request.GET.get('to')

    items = ShopItem.objects.filter(price__range=(from_number, to_number))

    return JsonResponse(create_dict_with_items(items))


def search_items(request):
    print(request.GET)
    return JsonResponse({'info':'Поиск работает'})

def search_item(request):
    searchWord = str(request.GET.get("searchWord"))
    items = Example.object.filter(name__containes=searchWord) 
    print(items)
    return JsonResponse(create_dict_with_items(items))

    

