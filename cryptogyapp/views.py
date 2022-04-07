import ast
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.template import loader

from .cryptosystems import rsa, rabin

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
    if request.is_ajax and request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RsaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            pParam = int(form.cleaned_data['primeP'])
            qParam = int(form.cleaned_data['primeQ'])
            cleartextParam = form.cleaned_data['clearText']
            ciphertextParam = form.cleaned_data['cipherText']
            print(request.POST)
            
            pubkey, privkey = rsa.gen_keys(pParam, qParam)
            if cleartextParam != "":
                # Encriptacion RSA
                print('Encriptado.')
                ciphertext = rsa.encrypt(cleartextParam, pubkey)
                ciphertext = ' '.join([str(x) for x in ciphertext])
                return JsonResponse({"ciphertext": ciphertext}, status=200)

            elif ciphertextParam != "":
                # Desencriptacion RSA
                print('Desencriptado.')
                ciphertextParam = [int(x.strip()) for x in ciphertextParam.split(' ')]
                print(ciphertextParam)
                try:
                    cleartext = rsa.decrypt(ciphertextParam, privkey)
                except Exception as e:
                    print("Error.")
                    return JsonResponse({"error": "Hubo un error."}, status=200)
                return JsonResponse({"cleartext": cleartext}, status=200)

            else:
                print("Error.")
                return JsonResponse({"error": "Hubo un error."}, status=200)

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
    if request.is_ajax and request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RsaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            pParam = int(form.cleaned_data['primeP'])
            qParam = int(form.cleaned_data['primeQ'])
            cleartextParam = form.cleaned_data['clearText']
            ciphertextParam = form.cleaned_data['cipherText']
            print(request.POST)
            
            pubkey, privkey = rsa.gen_keys(pParam, qParam)
            if cleartextParam != "":
                # Encriptacion Rabin
                print('Encriptado.')
                ciphertext = rabin.encrypt(cleartextParam, pubkey)
                ciphertext = ' '.join([str(x) for x in ciphertext])
                return JsonResponse({"ciphertext": ciphertext}, status=200)

            elif ciphertextParam != "":
                # Desencriptacion Rabin
                print('Desencriptado.')
                ciphertextParam = [int(x.strip()) for x in ciphertextParam.split(' ')]
                print(ciphertextParam)
                try:
                    cleartext = rabin.decrypt(ciphertextParam, privkey)
                except Exception as e:
                    print("Error.")
                    return JsonResponse({"error": "Hubo un error."}, status=200)
                return JsonResponse({"cleartext": cleartext}, status=200)

            else:
                print("Error.")
                return JsonResponse({"error": "Hubo un error."}, status=200)

        else:
            print("Invalid form.")


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

