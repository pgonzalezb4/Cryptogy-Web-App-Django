from sympy import randprime
from random import randint


def genParams(l, t):

    retry = True
    while retry:
        q = randprime(0, l)
        p = randprime(0, t)
        n = 0
        while ((p - 1) % q != 0) and (n < 100):
            p = randprime(0, t)
            n += 1
        if n < 100:
            retry = False

    h = randint(2, p - 2)
    g = pow(h, (p - 1) // q, p)
    while g == 1:
        h = randint(2, p - 2)
        g = pow(h, (p - 1) // q, p)

    return (p, q, g)


print(genParams(300, 300))
