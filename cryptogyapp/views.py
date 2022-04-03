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
    thisCryptosystem = Cryptosystem.objects.get(name="RSA")
    template = loader.get_template('cryptogyapp/rsa.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
    }
    return HttpResponse(template.render(context, request))

def rabinView(request):
    thisCryptosystem = Cryptosystem.objects.get(name="Rabin")
    template = loader.get_template('cryptogyapp/rabin.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
    }
    return HttpResponse(template.render(context, request))