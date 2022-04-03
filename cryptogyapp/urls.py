from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('RSA/', views.rsaView, name='rsacryptosystem'),
    path('Rabin/', views.rabinView, name='rabincryptosystem'),
]

