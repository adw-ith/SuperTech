from django.shortcuts import render
from .models import Category,Items,Tags

def home(request):
    items = Items.objects.all()
    context = {'items': items}
    return render(request, 'Items/Products.html',context)