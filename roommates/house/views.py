from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from core.models import UserProfile
from django.contrib.auth.models import User, Permission
from .forms import GroupForm, Join_Group_Form, CompletedForm
from .models import Group_Field, Group_Category, Group_User, Group, Assignment
#For Rust API
from rest_framework import viewsets
from rest_framework import permissions
from house.serializers import GroupSerializer, UserSerializer, AssignmentSerializer, GroupCategorySerializer
# Create your views here.

@login_required(login_url='/login/')
def house(request):
    this_user = Group_User.objects.filter(User = request.user)
    print("THIS GROUP: " + this_user[0].Group_Name)
    for person in Group_User.objects.all():
        if(person.Group_Name == this_user[0].Group_Name):
            print(person.User.username)

    if (request.GET.get('roommate')):
        user_info = request.GET['roommate']
        user_page = Group_User.objects.filter(id = user_info)
        user_page = user_page[0]
    else:
        user_page = this_user[0]

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

    current_user = Group_User.objects.filter(User = request.user);
    current_user = current_user[0]

    Assignments = Assignment.objects.all()
    members = Group_User.objects.all()
    group = this_user[0].Group_Name

    if (request.method == "GET" and "delete" in request.GET):
        pk = request.GET["delete"]
        group_to_delete = current_user.Group_Name
        for member in Group_User.objects.all():
            if member.Group_Name == group_to_delete:
                Group_User.objects.filter(User = member.User).delete()
                Group_User(User = member.User, Group_Name = "NULL").save()
        this_user = Group_User.objects.filter(User = request.user)
        user_page = this_user[0]
        group_to_delete = Group_Field.objects.filter(Group_Name = group_to_delete)
        group_to_delete[0].delete()
        current_user = Group_User.objects.filter(User = request.user);
        current_user = current_user[0]
        Assignments = Assignment.objects.all()
        members = Group_User.objects.all()
        group = this_user[0].Group_Name
        return render(request, 'house/house.html', {'group':group, 'members':members, "user_page":user_page, 'Assignments':Assignments, 'current_user':current_user})

    return render(request, 'house/house.html', {'group':group, 'members':members, "user_page":user_page, 'Assignments':Assignments, 'current_user':current_user})

@login_required(login_url='/login/')
def join_group(request):

    groups = Group_Field.objects.all()
    if (request.GET.get('join_group')):
        Group_User.objects.filter(User = request.user).delete()
        record = request.GET['join_group']
        Group_User(User=request.user, Group_Name=record).save()

    members = Group_User.objects.all()

    return render(request, 'house/join_group.html', {'groups':groups, 'members':members})

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
            Group_User.objects.filter(User = request.user).delete()
            Group_Field(User = request.user, Group_Name=group_name, Housing_Type=house).save()
            Group_User(User = request.user, Group_Name = group_name).save()
    group_form = GroupForm()
    return render(request, 'house/make_group.html', {'group_form': group_form})

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tasks to be viewed or edited.
    """
    queryset = Group_Field.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class AssignmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = Group_Category.objects.all()
    serializer_class = GroupCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
