from django.contrib import admin
from django.urls import path
from UserPortal import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('sign_up/', views.signup, name = 'sign_up'),
    path('create/', views.create, name = 'create'),
]