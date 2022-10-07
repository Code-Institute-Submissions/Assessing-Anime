from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.


class ItemList(generic.ListView):
    model = Item
    queryset = Item.objects.filter(status=1).order_by('-created_on')
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

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('animes:index')

    return render(request, 'animes/item-form.html', {'form': form})