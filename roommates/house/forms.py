from django import forms
from .models import Group_Field

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group_Field
        fields = ('Group_Name','Housing_Type')
