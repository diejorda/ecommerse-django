from unicodedata import category
from django.shortcuts import render, redirect
from .models import Item
from django.db.models import Q


# Create your views here.

def index(request):
    context={
        'items': Item.objects.all()
    }
    return render(request,'home-page.html', context)

def shirt(request):
    items=Item.objects.filter(category='S')
    
    context={
        'items': items
    }

    return render(request,'home-page.html' , context)

def ow(request):
    items=Item.objects.filter(category='OW')
    context={'items': items}

    return render(request,'home-page.html' , context)

def sw(request):
    items=Item.objects.filter(category='SW')
    context={'items': items}
    
    return render(request,'home-page.html' , context)

def search(request):
    if request.method == 'POST':
        search_parameter = request.POST['search-item']
        
        items= Item.objects.filter(Q(title__icontains=search_parameter)| Q(description__icontains=search_parameter) )
        context={'items': items}
    
        return render(request,'home-page.html' , context)
    else:
        return redirect('index')



def checkout(request):
    return render(request,'checkout-page.html',{})