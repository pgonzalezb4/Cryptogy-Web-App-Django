from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('RSA/', views.rsaView, name='rsacryptosystem'),
    path('Rabin/', views.rabinView, name='rabincryptosystem'),
    path('ElGamal/', views.elgamalView, name='elgamalcryptosystem'),
    path('Menezes-Vanstone/', views.menezesvanstoneView, name='menezesvanstonecryptosystem'),
    path('ElGamal-DSS/', views.elgamalDSSView, name='elgamaldsscryptosystem'),
    path('Menezes-Vanstone-DSS/', views.menezesvanstoneDSSView, name='menezesvanstonedsscryptosystem'),
]

