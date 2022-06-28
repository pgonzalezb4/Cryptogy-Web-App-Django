from random import randint
from .message import *


def encrypt(params, B, clear_text):

    p, q, g = params

    k = randint(2, p - 2)

    ciphertext = list()
    list_of_messages = string_to_nlist(clear_text, 4)

    for subtext in list_of_messages:
        m = string_to_int(subtext)

        c1 = pow(g, k, p)
        c2 = (m * pow(B, k, p)) % p

        ciphertext.append((c1, c2))

    return ciphertext


def decrypt(params, b, cipher_text):

    p, q, g = params

    cleartext = list()

    print(len(cipher_text), type(cipher_text))
    try:
        for c1, c2 in cipher_text:
            print("c1, c2:", c1, c2)
            print(type(c1), type(c2))
            m = (c2 * pow(pow(c1, b, p), -1, p)) % p
            print(m, type(m))
            cleartext.append(int_to_string(m))
    except Exception as e:
        print("Decryption error:", e)

    return "".join(cleartext)


def genKey(params):

    p, q, g = params

    a = randint(2, q - 2)

    A = pow(g, a, p)

    return (A, a)


if __name__ == "__main__":
    # TODO genParams() https://www.di-mgt.com.au/public-key-crypto-discrete-logs-1-diffie-hellman.html

    plain_message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"

    p = 19327210897467885519624495407304217845488409100133554803661172025039322784872775172789521895444178690740428588185031695453815386756662619555849446656794905221115788002016245291768283472480460523777510973085032471711187806590185987219179345022033106753600355795626394426859896564719805266547324204357196851217
    q = 983633858469108611936846792207646525014934079943
    g = 2008851267811649301382055697326002225321501629224616043097959307844472637339783779480891271906681929732776937543331689329117914118665148580824850572191418544875109802154341862162654424065963144063936607375606796563706389362731767772194368576684632589065496658911743756860379357301492526015846031839304359976

    params = (p, q, g)

    # Public Key
    # B = 216

    # Private Key
    # b = 7

    # Keys
    B, b = genKey(params)

    encrypted_message = encrypt(params, B, plain_message)
    print("Encrypted message:\n", encrypted_message)

    print(len(encrypted_message), type(encrypted_message))
    decrypted_message = decrypt(params, b, encrypted_message)
    print("Decrypted message:\n", decrypted_message)
