import random
import textwrap
from hashlib import sha512
from .message import *
from sympy import isprime

# generate a 128-bit prime number
def generate_a_prime_number(num_of_bits):
    # keep creating a random 16-byte (128-bit) number until there is a prime number
    while True:
        # randomly generate a 128-bit number
        num = random.getrandbits(num_of_bits)
        if isprime(num):
            return num
        else:
            continue


# Additional functions
class Key:
    def __init__(self, n, value):
        self.n = n
        self.value = value

    def __repr__(self) -> str:
        return "Key(%i, %i)" % (self.n, self.value)


def gcd(p, q):
    while q != 0:
        (p, q) = (q, p % q)
    return p


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


def gen_keys(p, q):
    if not isprime(p) or not isprime(q):
        return False

    n = p * q

    l = (p - 1) * (q - 1) // gcd(p - 1, q - 1)

    e = 1
    for i in range(l - 1, 1, -1):
        if gcd(i, l) == 1:
            e = i
            break

    # if 1 >= e or e >= l or gcd(e, l) != 1:
    #    return False

    # d = pow(e, -1, l)
    d = modinv(e, l)

    return (n, e), (n, d)


def encrypt(clear_text, public_key):
    n, value = public_key.n, public_key.value

    ciphertext = list()
    list_of_messages = [x + " " for x in textwrap.wrap(clear_text, 16)]

    for subtext in list_of_messages:

        m = string_to_int(subtext)
        c = pow(m, value, n)
        ciphertext.append(c)

    return ciphertext


def decrypt(cipher_text, private_key):
    n, value = private_key.n, private_key.value

    cleartext = list()

    for c in cipher_text:
        try:
            m = pow(c, value, n)
            cleartext.append(int_to_string(m))
        except:
            pass

    return "".join(cleartext)


if __name__ == "__main__":
    p = 1130846361230651253684643538702246078365421494379913454564820184574111462601735392110823359861485123092698624874028063966790975555365588590660366241420629
    q = 3203475635141361544530498295007148340563230674538615047974018284387630568724956766889573192829392408691707392765430948881758784937428126924812061361623139

    pub, priv = gen_keys(p, q)
    print(pub, priv)
    message = "Message to sign"
    bytes_message = str.encode(message)
    hash = int.from_bytes(sha512(bytes_message).digest(), byteorder="big")
    signature = pow(hash, priv[1], priv[0])
    print("Signature pre:", signature)
    print("Signature:", hex(signature))

    # Verificacion
    msg = "Message to sign tampered"
    bytes_msg = str.encode(msg)
    hash = int.from_bytes(sha512(bytes_msg).digest(), byteorder="big")
    hashFromSignature = pow(signature, pub[1], pub[0])
    print("Signature valid:", hash == hashFromSignature)
