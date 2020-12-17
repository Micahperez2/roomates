from django.contrib.auth.models import User
from house.models import Group, Group_User, Group_Field, Group_Category, Assignment
from django import forms

class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    username = forms.CharField(help_text=False)
    #email = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username':None
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class Add_Assignment(forms.ModelForm):
    class Meta():
        model = Assignment
        fields = ('Assignment_Name', 'Assignment_Description', 'Estimated_Time' )
