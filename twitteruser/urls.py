from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    
    path('profile/<int:user_id>', views.profile_view, name='profile')
    
]