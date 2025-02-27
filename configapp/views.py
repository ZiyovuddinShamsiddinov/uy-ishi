from django.shortcuts import render
from django.shortcuts import render
from  .models import *

def index(request):
    data=Actor.objects.all()
    data1=Movie.objects.all()
    contex={
        "db":data,
        "dc":data1,
        "title":"Ziyovuddin"

    }
    return render(request,'news/index.html',context=contex)



def batafsil(request, pk):
    data = Actor.objects.all()
    data1 = Movie.objects.all()
    context = {
        "db": data,
        "dc": data1,
        "title": "Ziyovuddin"
    }
    return render(request, 'news/batafsil.html', context=context)