from django.contrib import admin
from django.urls import path
from UserPortal import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('home/', views.home, name = 'home'),
    path('log_in/', views.user_login, name = 'login'),
    path('sign_up/', views.user_signup, name = 'signup'),
    path('log_out/', views.user_logout, name = 'logout'),
#     path('create/', views.create, name = 'create'),
#     path('update/int:<pk>', views.update, name = 'update'),
#     path('edit/int:<pk>', views.edit, name = 'edit'),
#     path('delete/int:<pk>', views.delete, name = 'delete'),
]