from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from core.models import UserProfile
from django.contrib.auth.models import User, Permission
from .forms import GroupForm
from .models import Group_Field, Group_Category, Group_User
#For Rust API
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.

@login_required(login_url='/login/')
def house(request):
    #for group in Group_Field.objects.all():
    #    print(group.Group_Name
    for person in Group_User.objects.all():
        print(person.User.username)
    return render(request, 'house/house.html')

@login_required(login_url='/login/')
def join_group(request):
    groups = Group_Field.objects.all()
    return render(request, 'house/join_group.html', {'groups':groups})

@login_required(login_url='/login/')
def make_group(request):
    if (not Group_Category.objects.all()):
        Group_Category.objects.create(category="House")
        Group_Category.objects.create(category="Apartment")
        Group_Category.objects.create(category="Dorm")
        Group_Category.objects.create(category="Individual Room")


    if (request.method == 'POST' and 'Submit_Group' in request.POST):
        form = GroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data["Group_Name"]
            house = form.cleaned_data["Housing_Type"]
            user = User.objects.get(id=request.user.id)
            Group_Field(User = user, Group_Name=group_name, Housing_Type=house).save()
            Group_User(User = user, Group_Name = group_name).save()
    group_form = GroupForm()
    return render(request, 'house/make_group.html', {'group_form': group_form})
