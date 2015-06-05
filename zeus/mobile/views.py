from django.http import HttpResponse
from django.template import Context, loader

__author__ = 'JunJianSyu'

def index(request):
    template = loader.get_template('index.html')
    context = Context({
        'request': request,
        'title': 'JunJianSyu',
    })
    return HttpResponse(template.render(context))