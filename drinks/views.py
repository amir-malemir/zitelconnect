from django.shortcuts import render
from django.views import generic

from .models import Drink

class DrinkListView(generic.ListView):
    model = Drink
    template_name = 'drinks/drinks.html'