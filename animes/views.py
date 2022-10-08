from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView

# Create your views here.


class ItemList(generic.ListView):
    model = Item
    queryset = Item.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'item_list'
    paginate_by = 6


class AnimeLikes(View):

    def anime(self, request, slug):
        anime = get_object_or_404(Item, slug=slug)

        if Item.likes.filter(id=request.user.id).exists():
            Item.likes.remove(request.user)
        else:
            Item.likes.add(request.user)

        return HttpResponseRedirect(reverse('index', args=[slug]))



def item(request):
    return HttpResponse('Item view')

def review(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }

    return render(request, 'review.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('animes:ItemList')

    return render(request, 'item-form.html', {'form': form})

