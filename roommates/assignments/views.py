from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from core.models import UserProfile
from django.contrib.auth.models import Group
from house.forms import GroupForm, Join_Group_Form, CompletedForm
from house.models import Group_Field, Group_Category, Group_User, Group, Assignment
#For Rust API
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.

@login_required(login_url='/login/')
def assignments(request):
    current_user = Group_User.objects.filter(User =  request.user)
    current_user = current_user[0].User
    Assignments = Assignment.objects.all()
    if (request.method == 'POST' and 'location' in request.POST):
        Completed_form = CompletedForm(request.POST)
        if Completed_form.is_valid():
            Key_number = Completed_form.cleaned_data.get("location")
            record = Assignment.objects.get(pk=Key_number)
            if (record.Completed == 'No'):
                record.Completed = 'Yes'
            else:
                record.Completed = 'No'
            record.save()

    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        deleted_assignment = Assignment.objects.filter(id=id)
        deleted_assignment[0].delete()

    return render(request, 'assignments/assignments.html', {'current_user':current_user, 'Assignments':Assignments})
