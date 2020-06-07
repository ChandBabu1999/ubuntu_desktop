from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from desktop.methods import create_folder, create_document
import os

def index(request):
    files = os.listdir("media")
    return render(request, 'desktop/home.html', {'documents': None, 'form': None})

@csrf_exempt
def menu_action(request):
    if request.POST['action'] == 'new_folder':
        name = request.POST['name']
        try: 
            create_folder(name)
            return HttpResponse('done (folder created in dir : media)', status='200')
        except:
            return HttpResponse('ERROR : (maybe folderName already  exist)', status='200')

    elif request.POST['action'] == 'new_doc':
        name = request.POST['name']
        try: 
            create_document(name)
            return HttpResponse('done (File created in dir : media)', status='200')
        except:
            return HttpResponse('error', status='400')

    elif request.POST['action'] == 'trash':
        return HttpResponse('done (File/Folder moved to trash)', status='200')
    else:
        return HttpResponse('error', status='404')