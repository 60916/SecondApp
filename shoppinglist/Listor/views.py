from django.shortcuts import render
from .models import List, Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Create your views here.
class AllaListor (LoginRequiredMixin,ListView):
  model=List
  template_name = 'listor/hem.html'
  context_object_name = 'listor'
  ordering = ['created_date']
  


