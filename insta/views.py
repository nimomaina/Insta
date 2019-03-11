from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.contrib.auth import views
from . models import *
from .forms import *

# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    pics = Picture.objects.all()
    profile = Profile.objects.all()
    return render(request,'home.html',locals())


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    pics = Picture.objects.all()
    profile = Profile.objects.all()

    return render(request, 'profile/profile.html',locals())

def form_upload(request):
    current_user= request.user
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.owner = current_user
            picture.save()
            return redirect('home')
    else:
        form = PictureForm()
    return render(request, 'upload.html', {'form': form})