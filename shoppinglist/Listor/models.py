from django.db import models
from django.utils import timezone 
import datetime
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    list_name = models.CharField(max_length=200)
    list_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.list_name


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    amount = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def _str_(self):
        return self.item_name
