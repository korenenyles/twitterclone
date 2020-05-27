from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('signup/', views.signUpView, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:user_id>', views.profile_view, name='profile')
    
]