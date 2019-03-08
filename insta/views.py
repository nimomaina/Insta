from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from . models import *
# Create your views here.



def home(request):
    return render(request,'home.html')