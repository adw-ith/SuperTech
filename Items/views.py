from django.shortcuts import render
from .models import Category,Items,Tags

def home(request):
    return render(request, 'Items/Products.html')