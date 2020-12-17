from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks_view_hide_completed = models.BooleanField(default=False)

class User_Minutes(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Time = models.IntegerField(default=0)
