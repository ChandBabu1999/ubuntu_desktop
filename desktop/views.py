from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, 'desktop/home.html', {'documents': None, 'form': None})

