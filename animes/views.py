from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }

    return render(request, 'animes/index.html', context)

def item(request):
    return HttpResponse('Item view')

def review(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }

    return render(request, 'animes/review.html', context)