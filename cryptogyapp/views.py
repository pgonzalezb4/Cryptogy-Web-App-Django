import re
import numpy as np
from PIL import Image
import textwrap


from hashlib import sha512

from django.http import HttpResponse, JsonResponse
from django.template import loader

from django.shortcuts import render

from .cryptosystems import blockchainsimulation, rsa, rsadss, rabin, menezesvanstone, elgamal, elgamaldss, vsss

from .models import Cryptosystem
from .forms import *

from django.conf import settings  

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
                pParam = rsa.generate_a_prime_number(512)
                qParam = rsa.generate_a_prime_number(512)
            
            pubkey, privkey = rsa.gen_keys(pParam, qParam)
            if cleartextParam != "":
                # Encriptacion RSA
                print('Encriptado.')
                try:
                    ciphertext = rsa.encrypt(cleartextParam, pubkey)
                    ciphertext = ' '.join([str(x) for x in ciphertext])
                    return JsonResponse({"ciphertext": ciphertext, "pParam" : str(pParam), "qParam" : str(qParam)}, status=200)
                except Exception as e:
                    print('Error:', e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)

            elif ciphertextParam != "":
                # Desencriptacion RSA
                print('Desencriptado.')
                try:
                    ciphertextParam = [int(x.strip()) for x in ciphertextParam.split(' ')]
                    try:
                        cleartext = rsa.decrypt(ciphertextParam, privkey)
                    except Exception as e:
                        print("Error.")
                        return JsonResponse({"error": "Hubo un error."}, status=200)
                    return JsonResponse({"cleartext": cleartext, "pParam" : pParam, "qParam" : qParam}, status=200)
                except Exception as e:
                    print('Error:', e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)

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
            pParam = form.cleaned_data['primeP']
            qParam = form.cleaned_data['primeQ']
            cleartextParam = form.cleaned_data['clearText']

            if len(cleartextParam) <= 2 and cleartextParam != '':
                cleartextParam += ' . .'

            cleartextParam = re.sub(r'[^\w\s]', '', cleartextParam)

            print(len(cleartextParam))
            ciphertextParam = form.cleaned_data['cipherText']
            print(request.POST)

            # Random key generator
            if pParam != '' and qParam != '':
                pParam = int(pParam)
                qParam = int(qParam)
            else:
                pParam = rabin.generate_a_prime_number(512)
                qParam = rabin.generate_a_prime_number(512)

            print('p:', pParam)
            print('q:', qParam)

            if cleartextParam != "":
                # Encriptacion Rabin
                print('Encriptado.')
                try:
                
                    print(cleartextParam)

                    if len(cleartextParam) > 64:
                        cleartextParam = textwrap.wrap(cleartextParam, 16)
                    else:
                        cleartextParam = [cleartextParam]

                    print(cleartextParam)
                    
                    ciphertext = []
                    for cltext in cleartextParam:
                        cltext = int.from_bytes(cltext.encode(), 'big')
                        cltext = rabin.encryption(cltext, pParam*qParam)
                        cltext = rabin.add_space(str(cltext))
                        ciphertext.append(cltext)

                    print(ciphertext)

                    ciphertext = ' | '.join(ciphertext)
                    return JsonResponse({"ciphertext": ciphertext, "pParam" : str(pParam), "qParam" : str(qParam)}, status=200)
                except Exception as e:
                    print('Error:', e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)

            elif ciphertextParam != "":
                # Desencriptacion Rabin
                print('Desencriptado.')
                try:
                    ciphertextParam = ciphertextParam.split(' | ')
                    print(ciphertextParam)

                    cleartext = []
                    for ciphtext in ciphertextParam:
                        ciphtext = int(rabin.delete_space(ciphtext))
                        cltext = int(format(rabin.decryption(ciphtext, pParam, qParam), 'x').zfill(226 // 4), 16)
                        cltext = cltext.to_bytes(((pParam*qParam).bit_length() + 7) // 8, 'big').decode('utf-8', 'strict')
                        cleartext.append(cltext)

                    cleartext = ' '.join([x.strip('\x00') for x in cleartext])
                    return JsonResponse({"cleartext": cleartext, "pParam" : pParam, "qParam" : qParam}, status=200)
                except Exception as e:
                    print('Error:', e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)

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
            pubKey = form.cleaned_data['pubKey']
            privKey = form.cleaned_data['privKey']
            cleartextParam = form.cleaned_data['clearText']
            ciphertextParam = form.cleaned_data['cipherText']
            print(request.POST)

            a = 2
            b = 9
            p = 37
            generator = (9, 4)

            params = (a, b, p)
            
            if pubKey != '' and privKey != '':
                alpha, k = int(pubKey), int(privKey)
            else:
                print('Generating keys...')
                alpha, k = menezesvanstone.generate_keys(params, generator, cleartextParam)

            print('Llaves:', alpha, k)
            if cleartextParam != "":
                # Encriptacion Menezes-Vanstone
                print('Encriptado.')
                try:
                    ciphertext = menezesvanstone.encrypt(cleartextParam, alpha, k, params, generator)
                    newCipherText = ''

                    for elem in ciphertext:
                        a, b = str(elem[0]), str(elem[1])
                        newCipherText += ('(' + a + ', ' + b + ')' + '; ') 

                    print(newCipherText)

                    return JsonResponse({"ciphertext": newCipherText, "alpha" : alpha, "k" : k}, status=200)
                except Exception as e:
                    print('Error:', e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)

            elif ciphertextParam != "":
                # Desencriptacion Menezes-Vanstone
                print('Desencriptado.')
                ciphertextParam = [x.strip() for x in ciphertextParam.split(';')][:-1]

                print(ciphertextParam)

                ciphertext = []
                for elem in ciphertextParam:
                    newElem = tuple(elem[1:-1].split(', '))
                    ciphertext.append(newElem)

                print(ciphertext)

                try:
                    cleartext = menezesvanstone.decrypt(ciphertext, alpha, params)

                except Exception as e:
                    print("Error:", e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)
                return JsonResponse({"cleartext": cleartext, "alpha" : alpha, "k" : k}, status=200)

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
            B = form.cleaned_data['pubKey']
            b = form.cleaned_data['privKey']
            cleartextParam = form.cleaned_data['clearText']
            ciphertextParam = form.cleaned_data['cipherText']
            print(request.POST)

            p = 19327210897467885519624495407304217845488409100133554803661172025039322784872775172789521895444178690740428588185031695453815386756662619555849446656794905221115788002016245291768283472480460523777510973085032471711187806590185987219179345022033106753600355795626394426859896564719805266547324204357196851217
            q = 983633858469108611936846792207646525014934079943
            g = 2008851267811649301382055697326002225321501629224616043097959307844472637339783779480891271906681929732776937543331689329117914118665148580824850572191418544875109802154341862162654424065963144063936607375606796563706389362731767772194368576684632589065496658911743756860379357301492526015846031839304359976
            params = (p, q, g)

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
                try:
                    ciphertext = elgamal.encrypt(params, B, cleartextParam)
                    
                    new_ciphertext = ''

                    for tup in ciphertext:
                        new_ciphertext += '--'.join([str(x) for x in list(tup)]) + '  '

                    return JsonResponse({"ciphertext": new_ciphertext, "pubkey" : str(B), "privkey" : str(b)}, status=200)
                except Exception as e:
                    print('Error:', e)
                    return JsonResponse({"error": "Hubo un error."}, status=200)

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

def copyFunction():
    print("Copiando")

def rsaDSSView(request):
    if request.is_ajax and request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RsaDSSForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()

            # process the data in form.cleaned_data as required
            pParam = form.cleaned_data['primeP']
            qParam = form.cleaned_data['primeQ']
            message = form.cleaned_data['message']
            signature = form.cleaned_data['signature']

            print(request.POST)
            # Random key generator
            if pParam != '' and qParam != '':
                pParam = int(pParam)
                qParam = int(qParam)
            else:
                pParam = rsadss.generate_a_prime_number(512)
                qParam = rsadss.generate_a_prime_number(512)
            
            pubkey, privkey = rsadss.gen_keys(pParam, qParam)
            n, e = pubkey
            n, d = privkey
            
            # Validacion
            if message != "" and signature != "":
                print('Validacion.')
                bytes_message = str.encode(message)
                hash = int.from_bytes(sha512(bytes_message).digest(), byteorder='big')
                hashFromSignature = pow(int(signature, base=16), e, n)
                if hash == hashFromSignature:
                    isValid = 'Signature validated'
                    print('Firma validada')
                else:
                    isValid = 'Signature not validated'
                return JsonResponse({"isValid": isValid, "pParam" : str(pParam), "qParam" : str(qParam)}, status=200)


            elif message != "":
                # Firma RSA
                print('Firma.')
                bytes_message = str.encode(message)
                hash = int.from_bytes(sha512(bytes_message).digest(), byteorder='big')
                signature = hex(pow(hash, d, n))
                return JsonResponse({"signature": signature, "pParam" : str(pParam), "qParam" : str(qParam)}, status=200)

            else:
                print("Error.")
                return JsonResponse({"error": "Hubo un error."}, status=200)

        else:
            print("Invalid form.")
            print(form.errors)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = RsaDSSForm()


    thisCryptosystem = Cryptosystem.objects.get(name="RSA-DSS")
    template = loader.get_template('cryptogyapp/rsa-dss.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def elgamalDSSView(request):
    if request.is_ajax and request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GammalDSSForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            B = form.cleaned_data['pubKey']
            b = form.cleaned_data['privKey']
            message = form.cleaned_data['message']
            signature = form.cleaned_data['signature']

            print(request.POST)

            p = 283
            q = 47
            g = 60
            params = (p, q, g)

            # Keys
            if B == '' and b == '':
                print("Generando nuevas claves...")
                B, b = elgamaldss.genKey(params)
            else:
                B = int(B)
                b = int(b)

            print("Claves:", B, b, type(B), type(b))

            if message != "" and signature != "":
                # Validación ElGammal
                new_signature = []

                for pair in signature.split('  '):
                    k = pair.split('--')
                    k = (int(k[0]), int(k[1]))
                    new_signature.append(k)

                print(new_signature)
                verification = elgamaldss.verify(params, B, message, new_signature)
                if verification:
                    isValid = 'Signature validated'
                else:
                    isValid = 'Signature not validated'

                return JsonResponse({"isValid": isValid, "pubkey" : str(B), "privkey" : str(b)}, status=200)

            elif message != "":
                # Firma ElGammal
                print('Firma.')
                signature = elgamaldss.sign(params, b, message)

                new_signature = ''

                for tup in signature:
                    new_signature += '--'.join([str(x) for x in list(tup)]) + '  '

                return JsonResponse({"signature": new_signature, "pubkey" : str(B), "privkey" : str(b)}, status=200)

            else:
                print("Error.")
                return JsonResponse({"error": "Hubo un error."}, status=200)

        else:
            print("Invalid form.")
            print(form.errors)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = GammalDSSForm()

    thisCryptosystem = Cryptosystem.objects.get(name="ElGamal-DSS")
    template = loader.get_template('cryptogyapp/elgamal-dss.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def imageEncryption(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ImageEncryptionForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():            
            form.save()    
            img_obj = form.instance  
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            if form.cleaned_data['clearImage']!=None and form.cleaned_data['cipherImageT1']==None and form.cleaned_data['cipherImageT2']==None:
                # try:
                vsss.encrypt_image(settings.BASE_DIR + img_obj.clearImage.url)
                print(settings.BASE_DIR + img_obj.clearImage.url)
                return render(request, 'imageencryption.html', {'form': form, 'img_obj': img_obj, 'img_t1': "/media/images/temp_img_t1.png", 'img_t2': "/media/images/temp_img_t2.png"})
                # except:
                #     return render(request, 'imageencryption.html', {'form': form})
            if form.cleaned_data['clearImage']==None and form.cleaned_data['cipherImageT1']!=None and form.cleaned_data['cipherImageT2']!=None:
                # try:
                vsss.decrypt_image(settings.BASE_DIR + img_obj.cipherImageT1.url,settings.BASE_DIR + img_obj.cipherImageT2.url)
                # except:
                #     return render(request, 'imageencryption.html', {'form': form})
                return render(request, 'imageencryption.html', {'form': form, 'img_obj': img_obj, 'clear_image': "/media/images/clear_image.png"})
        else:
            print("Invalid form.")
            print(form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ImageEncryptionForm()

    thisCryptosystem = Cryptosystem.objects.get(name="Image-Encryption")
    template = loader.get_template('cryptogyapp/imageencryption.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


blockchain = blockchainsimulation.Blockchain()

def blockchainSimulation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TransactionForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():            
            sender = form.cleaned_data['sender']
            receiver = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']
            message = form.cleaned_data['message']

            print('Transaction Info:', sender, receiver, amount, message)

            num = len(Block.objects.all())
            print(num)
            if num == 0:
                initial_block = blockchainsimulation.Block(0, data='Initial Block')
                blockchain.mine(initial_block)
                initial_block_obj = Block(number=initial_block.number, hash = initial_block.hash(), previous_hash = initial_block.previous_hash, 
                                    data = initial_block.data, nonce = initial_block.nonce, numoftransactions=0)
                initial_block_obj.save()
                transaction_obj = Transaction(sender=sender, receiver=receiver, amount=amount, message=message, block=initial_block_obj)
                transaction_obj.save()
                initial_block_obj.numoftransactions += 1
                initial_block_obj.save(update_fields=['numoftransactions'])

            else:
                last_block = Block.objects.get(number = num - 1)
                if last_block.numoftransactions < 2:
                    transaction_obj = Transaction(sender=sender, receiver=receiver, amount=amount, message=message, block=last_block)
                    transaction_obj.save()
                    last_block.numoftransactions += 1
                    last_block.save(update_fields=['numoftransactions'])
                else:
                    new_block = blockchainsimulation.Block(num, data=message)
                    blockchain.mine(new_block)
                    new_block_obj = Block(number=new_block.number, hash = new_block.hash(), previous_hash = new_block.previous_hash, data = new_block.data, 
                                        nonce = new_block.nonce, numoftransactions=0)
                    new_block_obj.save()
                    transaction_obj = Transaction(sender=sender, receiver=receiver, amount=amount, message=message, block=new_block_obj)
                    transaction_obj.save()
                    new_block_obj.numoftransactions += 1
                    new_block_obj.save(update_fields=['numoftransactions'])
            
        else:
            print("Invalid form.")
            print(form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransactionForm()

    all_transactions = Transaction.objects.all()
    thisCryptosystem = Cryptosystem.objects.get(name="Blockchain Simulation")
    template = loader.get_template('cryptogyapp/blockchainsimulation.html')
    context = {
        'thisCryptosystem': thisCryptosystem,
        'form': form,
        'transactions' : all_transactions,
    }
    return HttpResponse(template.render(context, request))

