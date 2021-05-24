from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('shop/', views.shop),
    path('contact/', views.contact),
    path('hangouts/', views.hangouts),
    path('login/', views.login),
]