__author__ = 'xujunjian'

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('hello junjian')
    content = {
        'title': '123',
    }
    return render(request, 'index.html', content)