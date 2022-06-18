
from django.urls import path
from.import views


urlpatterns = [
    path('songs',views.songs,name='songs' ),
    path('songs/<int:id>',views.songpost, name='songpost'),
    path('search', views.search, name='search')
    ]