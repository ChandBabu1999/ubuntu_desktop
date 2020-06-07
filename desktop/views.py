from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from desktop.methods import create_folder

def index(request):
    return render(request, 'desktop/home.html', {'documents': None, 'form': None})

@csrf_exempt
def menu_action(request):
    if request.POST['action'] == 'new_folder':
        name = request.POST['folder']
        try: 
            create_folder(name)
            return HttpResponse('done', status='200')
        except:
            return HttpResponse('error', status='400')
    else:
        return HttpResponse('error', status='404')