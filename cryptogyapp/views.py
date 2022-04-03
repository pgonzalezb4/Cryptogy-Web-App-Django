from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Cryptosystem

# Create your views here.

def index(request):
    cryptosystem_list = Cryptosystem.objects.all()
    template = loader.get_template('cryptogyapp/index.html')
    context = {
        'cryptosystem_list': cryptosystem_list,
    }
    return HttpResponse(template.render(context, request))

def rsaView(request):
    template = loader.get_template('cryptogyapp/rsa.html')
    context = {}
    return HttpResponse(template.render(context, request))

def rabinView(request):
    template = loader.get_template('cryptogyapp/rabin.html')
    context = {}
    return HttpResponse(template.render(context, request))