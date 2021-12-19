from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Max
from .models import *
#from .forms import *


def index(request):
    return HttpResponse('start page')
