from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from core.models import UserProfile, User_Minutes
from core.forms import JoinForm, LoginForm, Add_Assignment
from django.contrib.auth.models import User
from house.models import Group, Group_User, Group_Field, Group_Category, Assignment
# Create your views here.

@login_required(login_url='/login/')
def home(request):
    User_Minutes.objects.all().delete()
    try:
        (Group_User.objects.get(User_id=request.user.id))
    except:
        Group_User(User = User.objects.get(id=request.user.id), Group_Name = "NULL").save()
    group_users = Group_User.objects.all()
    for user in group_users:
        User_Minutes(User=user.User, Time = 0).save()
    for assignment in Assignment.objects.all():
        add_to = User_Minutes.objects.filter(User = assignment.User)
        total_time = add_to[0].Time + assignment.Estimated_Time
        this_user = add_to[0].User
        User_Minutes.objects.filter(User = assignment.User).delete()
        User_Minutes(User=this_user, Time = total_time).save()
    user_min = User_Minutes.objects.all()
    return render(request, 'core/home.html', {'group_users':group_users, 'user_min':user_min})

@login_required(login_url='/login/')
def add_assignment(request):
    if (request.method == 'POST' and 'Submit_Group' in request.POST):
        form = Add_Assignment(request.POST)
        if form.is_valid():
            assignment_name = form.cleaned_data["Assignment_Name"]
            assignment_description = form.cleaned_data["Assignment_Description"]
            estimated_time = form.cleaned_data["Estimated_Time"]
            Assignment(User = request.user, Assignment_Name=assignment_name, Assignment_Description=assignment_description, Estimated_Time=estimated_time, Completed = 'No').save()
    assignment_form = Add_Assignment
    return render(request, 'core/add_assignment.html', {'Add_Assignment' : Add_Assignment})

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = { "join_form": join_form }
            return render(request, 'core/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'core/join.html', page_data)

def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'core/login.html', {"login_form": LoginForm()})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'core/login.html', {"login_form": LoginForm() })

@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")
