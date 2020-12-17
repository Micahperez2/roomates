from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
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

class Assignment(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Assignment_Name = models.CharField(max_length=20)
    Assignment_Description = models.CharField(max_length=100)
    Estimated_Time =  models.IntegerField(default='0',
            validators=[
            MaxValueValidator(120),
            MinValueValidator(1)
        ]
     )
    COMPLETE = (
        ('Yes','Yes'),
        ('No','No'),
    )
    Completed = models.CharField(max_length=3, choices=COMPLETE, default='No')
