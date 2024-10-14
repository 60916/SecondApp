from django.shortcuts import render
from .models import List, Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

# Create your views here.
class AllaListor (LoginRequiredMixin,ListView):
  model=List
  template_name = 'listor/hem.html'
  context_object_name = 'listor'
  ordering = ['created_date']


class EnLista(LoginRequiredMixin,ListView):
  model=Item
  template_name = "listor/lista.html"
  context_object_name = 'items'

  def get_queryset(self):
    return Item.objects.filter(list=self.kwargs['pk'])
  
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context['listan'] = List.objects.filter(id=self.kwargs['pk'])
    return context
  
class NyLista(LoginRequiredMixin,CreateView):
  model = List
  fields = ['list_name']

