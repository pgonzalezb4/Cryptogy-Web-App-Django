from random import randint
import binascii


def string_to_nlist(text, n):
    list_of_messages = list()
    pos = 0
    while pos < len(text):
        try:
            list_of_messages.append(text[pos : pos + n])
            pos += n
        except:
            list_of_messages.append(text[pos : len(text)])
    return list_of_messages


def string_to_int(text):
    bits_ = string_to_bits(text)
    return int(bits_, 2)


def string_to_bits(text, encoding="utf-8", errors="surrogatepass"):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def int_to_string(i, encoding="utf-8", errors="surrogatepass"):
    try:
        bits = int_to_bits(i)
    except Exception as e:
        print("Error in int to bits:", e)
    return bits.decode(encoding, errors)


def int_to_bits(i):
    hex_string = "%x" % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


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

    try:
        for c1, c2 in cipher_text:
            m = (c2 * pow(pow(c1, b, p), -1, p)) % p
            cleartext.append(int_to_string(m))
    except Exception as e:
        print("Decryption error:", e)

    return "".join(cleartext)


def sign(params, b, clear_text):

    p, q, g = params

    signature = list()
    list_of_messages = string_to_nlist(clear_text, 4)

    while True:
        k = randint(0, p - 2)
        try:
            for subtext in list_of_messages:
                m = string_to_int(subtext)

                c1 = pow(g, k, p)
                c2 = ((m - b * c1) * pow(k, -1, (p - 1))) % (p - 1)

                signature.append((c1, c2))
        except:
            continue
        else:
            break

    return signature


def verify(params, B, clear_text, signature):

    p, q, g = params

    verification = list()
    list_of_messages = string_to_nlist(clear_text, 4)

    for c, subtext in zip(signature, list_of_messages):
        c1, c2 = c
        m = string_to_int(subtext)

        if (pow(B, c1) * pow(c1, c2)) % p != (pow(g, m, p)):
            return False

    return True


def genKey(params):

    p, q, g = params

    a = randint(2, q - 2)

    A = pow(g, a, p)

    return (A, a)


if __name__ == "__main__":
    # TODO genParams() https://www.di-mgt.com.au/public-key-crypto-discrete-logs-1-diffie-hellman.html

    plain_message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"

    # plain_message = "testing"

    p = 19327210897467885519624495407304217845488409100133554803661172025039322784872775172789521895444178690740428588185031695453815386756662619555849446656794905221115788002016245291768283472480460523777510973085032471711187806590185987219179345022033106753600355795626394426859896564719805266547324204357196851217
    q = 983633858469108611936846792207646525014934079943
    g = 2008851267811649301382055697326002225321501629224616043097959307844472637339783779480891271906681929732776937543331689329117914118665148580824850572191418544875109802154341862162654424065963144063936607375606796563706389362731767772194368576684632589065496658911743756860379357301492526015846031839304359976

    params = (p, q, g)

    p2 = 283
    q2 = 47
    g2 = 60

    params2 = (p2, q2, g2)

    # Keys
    B, b = genKey(params)
    B2, b2 = genKey(params2)

    encrypted_message = encrypt(params, B, plain_message)
    print("Encrypted message:\n", encrypted_message)

    print(len(encrypted_message), type(encrypted_message))
    decrypted_message = decrypt(params, b, encrypted_message)
    print("Decrypted message:\n", decrypted_message)

    signature = sign(params2, b2, plain_message)
    print("Signature:\n", signature)

    print(len(signature), type(signature))
    verification = verify(params2, B2, plain_message, signature)
    print("Verification:\n", verification)
