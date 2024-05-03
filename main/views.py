from typing import Any
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

#categories = Categories.objects.all()

# Create your views here.
def index(request):
    context = {
        'title': 'chicha home page',
        'content' : 'bueeeeeeeeeeeeee',

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'about chicha',
        'content' : 'main page - u r welcome',
        'text' : 'mad startup powered by shishaaaaaaaaaaaaaaaaaaaaaaaaaaaa4444444444444aaaaaaaaaaaaaaa'
    }
    return render(request, 'main/about.html', context)

