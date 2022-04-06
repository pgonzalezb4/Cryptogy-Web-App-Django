from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Cryptosystem
from .forms import RsaForm, RabinForm

# Create your views here.
def index(request):
    cryptosystem_list = Cryptosystem.objects.all()
    template = loader.get_template('cryptogyapp/index.html')
    context = {
        'cryptosystem_list': cryptosystem_list,
    }
    return HttpResponse(template.render(context, request))

def rsaView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("POST request.")
        # create a form instance and populate it with data from the request:
        form = RsaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("Debug.")
            # process the data in form.cleaned_data as required
            cd = form.cleaned_data
            p = cd['primeP']
            q = cd['primeQ']
            cleartext = cd['clearText']
            ciphertext = cd['cipherText']
            print(cd)
            # Encriptacion RSA
            if 'encrypt' in request.POST:
                pass # Codigo para encriptar...
            # Desencriptacion RSA
            elif 'decrypt' in request.POST:
                pass # Codigo para desencriptar...
            return HttpResponse('/RSA/')
        else:
            print("Form invalido.")


    # if a GET (or any other method) we'll create a blank form
    else:
        form = RsaForm()

    thisCryptosystem = Cryptosystem.objects.get(name="RSA")
    template = loader.get_template('cryptogyapp/rsa.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
        'form': form
    }
    return HttpResponse(template.render(context, request))

def rabinView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("POST request.")
        # create a form instance and populate it with data from the request:
        form = RabinForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cd = form.cleaned_data
            p = cd['primeP']
            q = cd['primeQ']
            cleartext = cd['clearText']
            ciphertext = cd['cipherText']
            print(cd)
            # Encriptacion Rabin
            if 'encrypt' in request.POST:
                pass # Codigo para encriptar...
            # Desencriptacion Rabin
            elif 'decrypt' in request.POST:
                pass # Codigo para desencriptar...
            return HttpResponse('/Rabin/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = RabinForm()

    thisCryptosystem = Cryptosystem.objects.get(name="Rabin")
    template = loader.get_template('cryptogyapp/rabin.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
        'form': form
    }
    return HttpResponse(template.render(context, request))

