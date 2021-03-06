from django.shortcuts import render, redirect
from .models import Item

# Create your views here.


def index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request,'personal-web/index.html', context)

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('index')
    return render( request, 'personal-web/add_item.html' )
