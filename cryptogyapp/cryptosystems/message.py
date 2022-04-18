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
        print(bits)
    except Exception as e:
        print("Error in int tobits:", e)
    return bits.decode(encoding, errors)


def int_to_bits(i):
    hex_string = "%x" % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
