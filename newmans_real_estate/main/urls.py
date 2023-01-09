from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('admin_login', views.admin),
    path('login', views.login),
    path('logout', views.logout),
    path('register', views.register),
    path('welcome_user', views.welcome_user),
]
