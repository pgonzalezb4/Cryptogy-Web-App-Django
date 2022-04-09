# 105064506 鄭柏偉 HW3
# Rabin Public-Key Cryptosystem

from . import prime, rabinutils

def delete_space(string):
    lst = string.split(' ')
    output = ''
    for i in lst:
        output += i
    return output


def add_space(string):
    string = string[::-1]
    string = ' '.join(string[i:i + 8] for i in range(0, len(string), 8))
    return string[::-1]


# main()
if __name__ == '__main__':

    ###########################################################
    # 256-bit prime number generation
    print('<Miller-Rabin>')
    print(add_space(format(prime.generate_a_prime_number(256), 'x')))

    ###########################################################
    # Encryption
    print('\n<Rabin Encryption>')

    # p and q has 128 bits
    p = int(delete_space(input('p = ')))   # p = daaefe652cad1614f17e87f2cd80973f (290680322482407050642711539016771082047)
    q = int(delete_space(input('q = ')))   # q = f99988626723eef2a54ed484dfa735c7 (331774958573786300819827599586292610503)
    n = p*q
    print('n = pq =', n)

    # plaintext has 224 bits
    # Rabin encryption
    inp = input('Plaintext = ')
    plaintext = int.from_bytes(inp.encode(), 'big') # plaintext = be000badbebadbadbad00debdeadfacedeafbeefadd00addbed00bed (20009354183959636439822187081543763705494133470478467066835281906669)
    ciphertext = rabinutils.encryption(plaintext, n)
    print('Ciphertext =', ciphertext)

    ###########################################################
    # Decryption
    print('\n<Rabin Decryption>')
    ciphertext = int(delete_space(input('Ciphertext = ')))    # 0x5452361adb4c34be04a5903ae00793bc1086e887ebed06e23ffba0b4a4348cc0
    print('Private Keys :')
    p = int(delete_space(input('p = ')))  # 0xd5e68b2b5855059ad1a80dd6c5dc03eb
    q = int(delete_space(input('q = ')))  # 0xc96c6afc57ce0f53396d3b32049fe2d3
    plaintext = int(format(rabinutils.decryption(ciphertext, p, q), 'x').zfill(226 // 4), 16)
    plaintext = plaintext.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print('Plaintext =', plaintext)