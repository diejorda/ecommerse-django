
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Item, CUser
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth



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


def signup(request):
    if request.method == 'POST':
        password=request.POST['pass1']
        password2=request.POST['pass2']
        username=request.POST['username']
        email=request.POST['email']
        
        
        if password != password2:
            messages.info(request, 'passwords dont match')
            return redirect('signup')

        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('signup')
        
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('signup')
        
        else:
            user= User.objects.create_user(email=email,username=username,password=password)
            user.save()
            user_login= auth.authenticate(username=username, password=password)
            auth.login(request,user_login)
            
            user_model= User.objects.get(username=username)
            cuser=CUser.objects.create(user=user_model)
            cuser.save()
            return redirect('index')
        
    else:
        return render(request,'signup.html',{})

    
def login(request):
    return redirect("index")


def checkout(request):
    return render(request,'checkout-page.html',{})