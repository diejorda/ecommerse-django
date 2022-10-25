from django.shortcuts import render

# Create your views here.

def item_list(request):
    context={
        'items': Item.objects.all()
    }
    render(requst,'item_list.html', context)