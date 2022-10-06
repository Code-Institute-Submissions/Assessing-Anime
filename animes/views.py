from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Item
from django.template import loader

# Create your views here.


class ItemList(generic.ListView):
    model = Item
    queryset = Item.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6

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