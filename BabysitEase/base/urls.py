from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    
    path('like/', views.favorited_babyssiter, name="favorited_babyssiter"),

]