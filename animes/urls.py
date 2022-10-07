from . import views
from django.urls import path

app_name = 'animes'
urlpatterns = [
    #/animes/
    path('', views.ItemList.as_view(), name='ItemList'),
    #/animes/1
    #path('item/', views.item, name='item'),
    #add items
    path('add', views.create_item, name='create_item'),
    #view likes
    path('like/<slug:slug>', views.AnimeLikes.as_view(), name='anime_likes'),
    path('<slug:slug>/', views.review, name='review'),
]
