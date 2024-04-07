from django.shortcuts import render
from .models import Category, Menu, Order
from django.views.generic import ListView, DetailView, ResultView


# Create your views here.

class MenuLV(ListView) :
    model = Menu

class MenuDV(DetailView) :
    model = Menu

class MenuRV(ResultView) :
    model = Order