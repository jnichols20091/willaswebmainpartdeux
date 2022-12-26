from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View

from Willlasweb import *


# Create your views here.
def print(request):
    return render(request, 'index.html')
