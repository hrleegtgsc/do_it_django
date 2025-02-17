from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.mypageIndex, name='mypage'),
    path('consulting/', views.consulting, name='consulting'),
    path('passwordUpdate/', views.passwordUpdate, name='passwordUpdate'),
    path('userinfoUpdate/', views.userinfoUpdate, name='userinfoUpdate'),
    path('mypageadmin/', views.mypageAdmin, name='mypageAdmin')
]
