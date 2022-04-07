import binascii
import random


def isPrime(mrc):
    """Run 20 iterations of Rabin Miller Primality test"""
    maxDivisionsByTwo = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert 2**maxDivisionsByTwo * ec == mrc - 1

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc - 1:
                return False
        return True

    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


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
    if not isPrime(p) or not isPrime(q):
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


def string_to_4list(text):
    list_of_messages = list()
    pos = 0
    while pos < len(text):
        try:
            list_of_messages.append(text[pos : pos + 4])
            pos += 4
        except:
            list_of_messages.append(text[pos : len(text)])
    return list_of_messages


def string2int(text):
    bits_ = text_to_bits(text)
    return int(bits_, 2)


def text_to_bits(text, encoding="utf-8", errors="surrogatepass"):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def int2bytes(i):
    hex_string = "%x" % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def int2string(i, encoding="utf-8", errors="surrogatepass"):
    print('Input', i)
    bytes_ = int2bytes(i)
    print('Bytes', bytes_)
    return bytes_.decode(encoding, errors)


def encrypt(clear_text, public_key):
    n, value = public_key.n, public_key.value

    ciphertext = list()
    list_of_messages = string_to_4list(clear_text)

    for subtext in list_of_messages:

        m = string2int(subtext)
        c = pow(m, value, n)
        ciphertext.append(c)

    return ciphertext


def decrypt(cipher_text, private_key):
    n, value = private_key.n, private_key.value

    cleartext = list()

    for c in cipher_text:
        m = pow(c, value, n)
        cleartext.append(int2string(m))

    return "".join(cleartext)


if __name__ == "__main__":

    p = 598523229523791300517772583157
    q = 735983657699353304370886992107

    pub, priv = gen_keys(p, q)
    print(pub, priv)
    print(
        encrypt(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
            pub,
        )
    )
    print(
        encrypt(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
            pub,
        )
    )
