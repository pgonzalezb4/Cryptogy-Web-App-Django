import random
from sympy import randprime

# Helper Functions
char_to_point = {
    "a": (5, 25),
    "b": (1, 30),
    "c": (21, 32),
    "d": (7, 25),
    "e": (25, 12),
    "f": (4, 28),
    "g": (0, 34),
    "h": (16, 17),
    "i": (15, 26),
    "j": (27, 32),
    "k": (9, 4),
    "l": (2, 24),
    "m": (26, 5),
    "n": (33, 14),
    "o": (11, 17),
    "p": (31, 22),
    "q": (13, 30),
    "r": (35, 21),
    "s": (23, 7),
    "t": (10, 17),
    "u": (29, 6),
    "v": (29, 31),
    "w": (10, 20),
    "x": (23, 30),
    "y": (35, 16),
    "z": (13, 7),
    "1": (31, 15),
    "2": (11, 20),
    "3": (33, 23),
    "4": (26, 32),
    "5": (2, 13),
    "6": (9, 33),
    "7": (27, 5),
    "8": (15, 11),
    "9": (16, 20),
    "0": (0, 3),
    "#": (4, 9),
    "@": (25, 25),
    "!": (7, 12),
    "&": (21, 5),
    "$": (1, 7),
    "%": (5, 12),
}

point_to_char = {
    (5, 25): "a",
    (1, 30): "b",
    (21, 32): "c",
    (7, 25): "d",
    (25, 12): "e",
    (4, 28): "f",
    (0, 34): "g",
    (16, 17): "h",
    (15, 26): "i",
    (27, 32): "j",
    (9, 4): "k",
    (2, 24): "l",
    (26, 5): "m",
    (33, 14): "n",
    (11, 17): "o",
    (31, 22): "p",
    (13, 30): "q",
    (35, 21): "r",
    (23, 7): "s",
    (10, 17): "t",
    (29, 6): "u",
    (29, 31): "v",
    (10, 20): "w",
    (23, 30): "x",
    (35, 16): "y",
    (13, 7): "z",
    (31, 15): "1",
    (11, 20): "2",
    (33, 23): "3",
    (26, 32): "4",
    (2, 13): "5",
    (9, 33): "6",
    (27, 5): "7",
    (15, 11): "8",
    (16, 20): "9",
    (0, 3): "0",
    (4, 9): "#",
    (25, 25): "@",
    (7, 12): "!",
    (21, 5): "&",
    (1, 7): "$",
    (5, 12): "%",
}


def get_points(a: int, b: int, p: int):

    return [
        (x, y)
        for x in range(p)
        for y in range(p)
        if (y ** 2 - (x ** 3 + (a * x) + b)) % p == 0
    ]


def check_params(a: int, b: int, p: int, generator: tuple):

    if 4 * a ** 3 + 27 * b ** 2 % p != 0:
        points = get_points(a, b, p)

        if generator in points:
            return True

        else:
            raise Exception("Generator not in curve.")
    else:
        raise Exception("a and b do not satisfy requirements.")


# PARAMETERS and KEYS Generator.
def generate_params():

    a = random.randint(0, 100)
    b = random.randint(0, 100)
    p = randprime(1, 1000)

    while 4 * a ** 3 + 27 * b ** 2 % p == 0:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        p = randprime(1, 1000)

    cycle = get_points(a, b, p)
    generator = random.choice(cycle)

    return (a, b, p, generator)


def generate_keys(a: int, b: int, p: int):

    cycle = get_points(a, b, p)

    alpha = random.randint(0, len(cycle))
    k = random.randint(0, len(cycle))

    return (alpha, k)


# Cycle Generator
def generate_cycle(generator: tuple, params: tuple):
    cycle = [generator]
    np = add(generator, generator, params)
    cycle.append(np)
    while np[0] != generator[0]:
        np = add(np, generator, params)
        cycle.append(np)
    cycle.append("O")
    return cycle


def add(p1: tuple, p2: tuple, params: tuple):
    a = params[0]
    p = params[2]

    if p1 == p2:
        h = ((3 * p1[0] ** 2 + a) % p * pow(2 * p1[1], -1, p)) % p
    else:
        h = ((p2[1] - p1[1]) % p * pow(p2[0] - p1[0], -1, p)) % p

    x3 = (h ** 2 - p1[0] - p2[0]) % p
    y3 = (h * (p1[0] - x3) - p1[1]) % p

    return (x3, y3)


def key_gen(key: int, cycle: list):
    key = key % p
    if key == 0:
        return cycle[-1]
    return cycle[key - 1]


def encrypt(message: str, alpha: int, k: int, params: tuple, generator: tuple):

    ciphertext = list()
    for char in message:
        char = char.lower()

        if char not in char_to_point:
            ciphertext.append(("O", "O"))
            continue

        b = key_gen(alpha, generate_cycle(generator, params))
        x = key_gen(k, generate_cycle(generator, params))
        y = add(char_to_point[char], key_gen(k, generate_cycle(b, params)), params)

        ciphertext.append((point_to_char[x], point_to_char[y]))
    return ciphertext


def decrypt(cipher_text: list, alpha: int, params: tuple):

    cleartext = list()

    for x, y in cipher_text:

        if x not in char_to_point or y not in char_to_point:
            cleartext.append(" ")
            continue

        r = add(
            char_to_point[y],
            generate_cycle(
                key_gen(alpha, generate_cycle(char_to_point[x], params)), params
            )[-2],
            params,
        )
        cleartext.append(point_to_char[r])
    return "".join(cleartext)


if __name__ == "__main__":
    # a = 1
    # b = 6
    # p = 11
    # generator = (2, 7)

    a = 2
    b = 9
    p = 37
    generator = (9, 4)

    if check_params(a, b, p, generator):
        params = (a, b, p)
    else:
        raise ("incorrect params")

    # message = (5, 25)
    message = "this is a completely random clear text to test the menezes vanstone cryptosystem encryption process"
    alpha, k = generate_keys(a, b, p)

    print("encrypting", message)
    e = encrypt(message, alpha, k, params, generator)
    print(e)

    print()

    print("decrypting", e)
    d = decrypt(e, alpha, params)
    print(d)
