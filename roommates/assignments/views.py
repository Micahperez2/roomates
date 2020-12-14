from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from core.models import UserProfile
from django.contrib.auth.models import Group
#For Rust API
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.

@login_required(login_url='/login/')
def assignments(request):
    return render(request, 'assignments/assignments.html')
