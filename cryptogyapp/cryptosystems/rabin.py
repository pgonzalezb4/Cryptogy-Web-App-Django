import random
import sys

sys.path.insert(0, r"cryptogyapp")
from sympy import isprime

# PARAMETERS
# generate a n-bit prime number
def generate_a_prime_number(num_of_bits):
    # keep creating a random (n/8)-byte (n-bit) number until there is a prime number
    while 1:
        # randomly generate a n-bit number
        num = random.getrandbits(num_of_bits)
        if isprime(num) and (num % 4) == 3:
            return num
        else:
            continue

# Find SQROOT in Zp where p = 3 mod 4
def sqrt_p_3_mod_4(a, p):
    r = pow(a, (p + 1) // 4, p)
    return r

# Find SQROOT in Zp where p = 5 mod 8
def sqrt_p_5_mod_8(a, p):
    d = pow(a, (p - 1) // 4, p)
    r = 0
    if d == 1:
        r = pow(a, (p + 3) // 8, p)
    elif d == p - 1:
        r = 2 * a * pow(4 * a, (p - 5) // 8, p) % p

    return r

# Legendre symbol
def Legendre(a, p):
    return pow(a, (p - 1) / 2, p)

#
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, y, x = egcd(b % a, a)
        return gcd, x - (b // a) * y, y

# Additional functions
def none_in_x_is_n(x, n):
    for i in x:
        if i == n:
            return False
    return True

# encryption function
# plaintext is a 224-bit number
def encryption(plaintext, n):
    # c = m^2 mod n
    plaintext = padding(plaintext)
    return plaintext ** 2 % n

# padding 16 bits to the end of a number
def padding(plaintext):
    binary_str = bin(plaintext)  # convert to a bit string
    output = binary_str + binary_str[-16:]  # pad the last 16 bits to the end
    return int(output, 2)  # convert back to integer

# encryption function
def decryption(a, p, q):
    n = p * q
    r, s = 0, 0
    # find sqrt
    # for p
    if p % 4 == 3:
        r = sqrt_p_3_mod_4(a, p)
    elif p % 8 == 5:
        r = sqrt_p_5_mod_8(a, p)
    # for q
    if q % 4 == 3:
        s = sqrt_p_3_mod_4(a, q)
    elif q % 8 == 5:
        s = sqrt_p_5_mod_8(a, q)

    gcd, c, d = egcd(p, q)
    x = (r * d * q + s * c * p) % n
    y = (r * d * q - s * c * p) % n
    lst = [x, n - x, y, n - y]

    plaintext = choose(lst)
    string = bin(plaintext)
    string = string[:-16]
    plaintext = int(string, 2)

    return plaintext

# decide which answer to choose
def choose(lst):
    for i in lst:
        binary = bin(i)
        append = binary[-16:]  # take the last 16 bits
        binary = binary[:-16]  # remove the last 16 bits
        if append == binary[-16:]:
            return i
    return

def delete_space(string):
    lst = string.split(" ")
    output = ""
    for i in lst:
        output += i
    return output

def add_space(string):
    string = string[::-1]
    string = " ".join(string[i : i + 8] for i in range(0, len(string), 8))
    return string[::-1]

# main()
if __name__ == "__main__":

    ###########################################################
    # 256-bit prime number generation
    print("<Miller-Rabin>")
    print(add_space(format(generate_a_prime_number(256), "x")))

    ###########################################################
    # Encryption
    print("\n<Rabin Encryption>")

    # p and q has 128 bits
    p = int(
        delete_space(input("p = "))
    )  # p = daaefe652cad1614f17e87f2cd80973f (290680322482407050642711539016771082047)
    q = int(
        delete_space(input("q = "))
    )  # q = f99988626723eef2a54ed484dfa735c7 (331774958573786300819827599586292610503)
    p = generate_a_prime_number(128)
    q = generate_a_prime_number(128)
    print("p:", p)
    print("q:", q)
    n = p * q
    print("n = pq =", n)

    # plaintext has 224 bits
    # Rabin encryption
    inp = input("Plaintext = ")
    plaintext = int.from_bytes(
        inp.encode(), "big"
    )  # plaintext = be000badbebadbadbad00debdeadfacedeafbeefadd00addbed00bed (20009354183959636439822187081543763705494133470478467066835281906669)
    ciphertext = encryption(plaintext, n)
    print("Ciphertext =", add_space(str(ciphertext)))

    ###########################################################
    # Decryption
    print("\n<Rabin Decryption>")
    ciphertext = int(
        delete_space(input("Ciphertext = "))
    )  # 0x5452361adb4c34be04a5903ae00793bc1086e887ebed06e23ffba0b4a4348cc0
    print("Private Keys :")
    p = int(delete_space(input("p = ")))  # 0xd5e68b2b5855059ad1a80dd6c5dc03eb
    q = int(delete_space(input("q = ")))  # 0xc96c6afc57ce0f53396d3b32049fe2d3
    plaintext = int(format(decryption(ciphertext, p, q), "x").zfill(226 // 4), 16)
    plaintext = plaintext.to_bytes((n.bit_length() + 7) // 8, "big").decode()
    print("Plaintext =", plaintext)
