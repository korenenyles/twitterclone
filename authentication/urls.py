from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
path('signup/', views.SignUpView.as_view(), name='signup'),
path('login/', views.loginview, name='login'),
path('logout/', views.logout_view, name='logout'),
]