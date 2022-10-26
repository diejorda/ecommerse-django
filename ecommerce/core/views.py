from django.shortcuts import render
from .models import Item

# Create your views here.

def index(request):
    context={
        'items': Item.objects.all()
    }
    return render(request,'home-page.html', context)

def checkout(request):
    return render(request,'checkout-page.html',{})