import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.template import loader

from .models import Cryptosystem
from .forms import RsaForm, RabinForm

def encryptRsa(p, q, cleartext):
    return 'ciphertext sample.'

def decryptRsa(p, q, ciphertext):
    return 'cleartext sample.'

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
    if request.is_ajax and request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RsaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            pParam = form.cleaned_data['primeP']
            qParam = form.cleaned_data['primeQ']
            cleartextParam = form.cleaned_data['clearText']
            ciphertextParam = form.cleaned_data['cipherText']
            print(request.POST)
            if request.POST.get('encrypt'):
                # Encriptacion RSA
                print('Encriptado.')
                ciphertext = encryptRsa(pParam, qParam, cleartextParam)

            elif request.POST.get('decrypt'):
                # Desencriptacion RSA
                print('Desencriptado.')
                cleartext = decryptRsa(pParam, qParam, ciphertextParam)

            ciphertext = "Sample cipher text."
            return JsonResponse({"ciphertext": ciphertext}, status=200)
        else:
            print("Invalid form.")


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
            return render(request, 'cryptogyapp/rabin.html', {"form": form})
        else:
            print('Invalid form.')


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

