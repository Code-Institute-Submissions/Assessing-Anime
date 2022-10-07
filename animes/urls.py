from . import views
from django.urls import path

app_name = 'animes'
urlpatterns = [
    #/animes/
    path('', views.index, name='index'),
    #/animes/1
    path('<int:item_id>', views.review, name='review'),
    path('item/', views.item, name='item'),
    #add items
    path('add', views.create_item, name='create_item'),

]
