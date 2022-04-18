import string

from django.http import HttpResponse, JsonResponse
from django.template import loader

from .cryptosystems import rsa, rabin, menezesvanstone, elgamal

from .models import Cryptosystem
from .forms import *

# Create your views here.
def index(request):
    cryptosystem_list = Cryptosystem.objects.all()
    template = loader.get_template('cryptogyapp/index.html')
    context = {
        'cryptosystem_list': cryptosystem_list
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

            # Random key generator
            

            if pParam != '' and qParam != '':
                pParam = int(pParam)
                qParam = int(qParam)
            else:
                pParam = rsa.generate_a_prime_number(256)
                qParam = rsa.generate_a_prime_number(256)
            
            pubkey, privkey = rsa.gen_keys(pParam, qParam)
            if cleartextParam != "":
                # Encriptacion RSA
                print('Encriptado.')
                ciphertext = rsa.encrypt(cleartextParam, pubkey)
                ciphertext = ' '.join([str(x) for x in ciphertext])
                return JsonResponse({"ciphertext": ciphertext, "pParam" : str(pParam), "qParam" : str(qParam)}, status=200)

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
                return JsonResponse({"cleartext": cleartext, "pParam" : pParam, "qParam" : qParam}, status=200)

            else:
                print("Error.")
                return JsonResponse({"error": "Hubo un error."}, status=200)

        else:
            print("Invalid form.")
            print(form.errors)


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
            pParam = int(rabin.delete_space(str(form.cleaned_data['primeP'])))
            qParam = int(rabin.delete_space(str(form.cleaned_data['primeQ'])))
            cleartextParam = form.cleaned_data['clearText']
            ciphertextParam = form.cleaned_data['cipherText']
            print(request.POST)
            
            if cleartextParam != "":
                # Encriptacion Rabin
                print('Encriptado.')
                cleartextParam = int.from_bytes(cleartextParam.encode(), 'big')
                ciphertext = rabin.encryption(cleartextParam, pParam*qParam)
                ciphertext = rabin.add_space(str(ciphertext))
                return JsonResponse({"ciphertext": ciphertext}, status=200)

            elif ciphertextParam != "":
                # Desencriptacion Rabin
                print('Desencriptado.')
                ciphertextParam = int(rabin.delete_space(ciphertextParam))
                print(ciphertextParam)
                try:
                    cleartext = int(format(rabin.decryption(ciphertextParam, pParam, qParam), 'x').zfill(226 // 4), 16)
                    cleartext = cleartext.to_bytes(((pParam*qParam).bit_length() + 7) // 8, 'big').decode('utf-8', 'strict')
                except Exception as e:
                    print("Error:", e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)
                return JsonResponse({"cleartext": cleartext}, status=200)

            else:
                print("Error.")
                return JsonResponse({"error": "Hubo un error."}, status=200)

        else:
            print("Invalid form.")
            print(form.errors)


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

def menezesvanstoneView(request):
    if request.is_ajax and request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MVForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cleartextParam = form.cleaned_data['clearText']
            ciphertextParam = form.cleaned_data['cipherText']
            keyParam = form.cleaned_data['keyParam']
            print(request.POST)
            
            if keyParam != '':
                key = [int(x.strip()) for x in keyParam.split(',')]
                print("Key:", key)
                cipher = menezesvanstone.MenezesVanstoneCipher(key)
            else:
                cipher = menezesvanstone.MenezesVanstoneCipher(None)
                key = cipher.key
                print(key)

            if cleartextParam != "":
                # Encriptacion Menezes-Vanstone
                print('Encriptado.')
                cleartextParam = cleartextParam.translate(str.maketrans('', '', string.punctuation))
                cleartextParam = cleartextParam.split(' ')

                ciphertext = []
                for text in cleartextParam:
                    ciphertext.append(cipher.encode(text))

                ciphertext = '  '.join(ciphertext)

                return JsonResponse({"ciphertext": ciphertext, "key" : key}, status=200)

            elif ciphertextParam != "":
                # Desencriptacion Menezes-Vanstone
                print('Desencriptado.')

                try:
                    ciphertextParam = ciphertextParam.split('  ')

                    cleartext = []
                    for text in ciphertextParam:
                        cleartext.append(cipher.decode(text))

                    cleartext = ' '.join(cleartext)
                except Exception as e:
                    print("Error:", e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)
                return JsonResponse({"cleartext": cleartext.lower().capitalize()}, status=200)

            else:
                print("Error.")
                return JsonResponse({"error": "Hubo un error."}, status=200)

        else:
            print("Invalid form.")
            print(form.errors)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = MVForm()

    thisCryptosystem = Cryptosystem.objects.get(name="Menezes-Vanstone")
    template = loader.get_template('cryptogyapp/menezes-vanstone.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
        'form': form
    }
    return HttpResponse(template.render(context, request))

def elgamalView(request):
    if request.is_ajax and request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GammalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            pNumber = int(form.cleaned_data['pNumber'])
            qNumber = int(form.cleaned_data['qNumber'])
            gNumber = int(form.cleaned_data['gNumber'])
            B = form.cleaned_data['pubKey']
            b = form.cleaned_data['privKey']
            cleartextParam = form.cleaned_data['clearText']
            ciphertextParam = form.cleaned_data['cipherText']
            print(request.POST)
            
            params = (pNumber, qNumber, gNumber)

            # Keys
            if B == '' and b == '':
                print("Generando nuevas claves...")
                B, b = elgamal.genKey(params)
            else:
                B = int(B)
                b = int(b)

            print("Claves:", B, b, type(B), type(b))
            if cleartextParam != "":
                # Encriptacion ElGammal
                print('Encriptado.')
                ciphertext = elgamal.encrypt(params, B, cleartextParam)
                
                new_ciphertext = ''

                for tup in ciphertext:
                    new_ciphertext += '--'.join([str(x) for x in list(tup)]) + '  '

                return JsonResponse({"ciphertext": new_ciphertext, "pubkey" : str(B), "privkey" : str(b)}, status=200)

            elif ciphertextParam != "":
                # Desencriptacion ElGammal
                print('Desencriptado.')
                ciphertextParam = ciphertextParam.split('  ')

                ciphertext = []
                for ciphert in ciphertextParam:
                    newl = [int(x) for x in ciphert.split('--')]
                    newl = tuple(newl)
                    ciphertext.append(newl)

                try:
                    cleartext = elgamal.decrypt(params, b, ciphertext)
                except Exception as e:
                    print("Error:", e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)
                return JsonResponse({"cleartext": cleartext}, status=200)

            else:
                print("Error.")
                return JsonResponse({"error": "Hubo un error."}, status=200)

        else:
            print("Invalid form.")
            print(form.errors)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = GammalForm()

    thisCryptosystem = Cryptosystem.objects.get(name="ElGamal")
    template = loader.get_template('cryptogyapp/elgamal.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
        'form': form
    }
    return HttpResponse(template.render(context, request))
