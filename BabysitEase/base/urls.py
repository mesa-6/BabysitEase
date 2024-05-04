from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('like/<str:pk>/', views.favorited_babyssiter, name="favorited_babyssiter"),
    path('babysitter-dtl/<str:pk>/', views.BabysitterDetailView.as_view(), name="babysitter_details"),
    path('editar-perfil/', views.PerfilUpdate.as_view(), name="editar-perfil"),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('schedules-solicitation/', views.schedules_solicitation, name='schedules-solicitation'),
]