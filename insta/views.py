from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.contrib.auth import views
from . models import *
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    pics = Picture.objects.all()
    profile = Profile.objects.all()
    return render(request,'home.html',locals())

def profile(request):
    return render(request, profile/profile.html)