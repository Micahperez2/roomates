from django import forms
from .models import Group_Field

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group_Field
        fields = ('Group_Name','Housing_Type')

class Join_Group_Form(forms.Form):
    key=forms.CharField()

class CompletedForm(forms.Form):
     location=forms.CharField()
