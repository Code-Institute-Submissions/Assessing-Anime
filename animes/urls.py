from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>',views.review,name='review'),
    path('item/', views.item, name='item'),
]
