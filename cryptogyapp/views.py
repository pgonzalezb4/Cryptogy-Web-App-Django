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
    return HttpResponse("RSA cryptosystem view.")

def rabinView(request):
    return HttpResponse("Rabin cryptosystem view.")