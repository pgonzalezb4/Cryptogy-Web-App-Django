import random
import textwrap
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
        raise Exception('modular inverse does not exist')
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

    #d = pow(e, -1, l)
    d = modinv(e, l)

    return Key(n, e), Key(n, d)

def encrypt(clear_text, public_key):
    n, value = public_key.n, public_key.value

    ciphertext = list()
    list_of_messages = [x + ' ' for x in textwrap.wrap(clear_text, 16)]

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
    p = 8258171947
    q = 5891608337

    pub, priv = gen_keys(p, q)
    print(pub, priv)
    print(
        encrypt(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
            pub,
        )
    )
    print(
        decrypt(
        encrypt(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
            pub,
        ), priv)
    )
