from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Group_Category(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category

class Group_Field(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Group_Name = models.CharField(max_length=20)
    Housing_Type = models.ForeignKey(Group_Category, on_delete=models.CASCADE)

class Group(models.Model):
    Name = models.CharField(max_length=20)

class Group_User(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Group_Name = models.CharField(max_length=25)
    #ID = models.IntegerField()
    #Name = models.CharField(max_length=25)
    #Matching_Group = models.ForeignKey(Group_Category, on_delete=models.CASCADE)
