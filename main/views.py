from typing import Any
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home sweet home',
        'content' : 'main page - u r welcome'
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('about')
