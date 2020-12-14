from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class JOURNAL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField(auto_now=True)
    Description = models.CharField(max_length=50)
    Entry = models.CharField(max_length=300)
