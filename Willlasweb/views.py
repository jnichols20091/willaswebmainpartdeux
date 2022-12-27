from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View

from Willlasweb import *


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about_me(request):
    return render(request, 'about_me.html')

def contact(request):
    return render(request, 'contact.html')

