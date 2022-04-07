import sympy as sy
import random
from subprocess import call

p2 = 0
q2 = 0
p1 = 0
q1 = 0
n = 0
entero1 = 0
cifrado = 0

def cifrar(mensaje):                     #esta funcion cifra el mensaje
    primos=[]
    for t in range(30,1000):              #este for genera primos aleatoriamente, congruentes con 3 modulo 4
        if sy.isprime(t):
            if t%4==3:
                primos.append(t)
    
    global p2
    global q2
    global p1
    global q1
    p2=p1=(primos[random.randint(0,len(primos)-1)])    #p y q tomados al azar de la lista de primos congruentes 3 modulo 4
    q2=q1=(primos[random.randint(0,len(primos)-1)])
    
    global n
    n = p2*q2
    mensajebinario = bin(int.from_bytes(mensaje.encode(), 'big')) #convierte el mensaje a binario
    entero = int(mensajebinario, base=2)                            #convierte el binario a entero
    global entero1
    entero1 = bin(int.from_bytes(mensaje.encode(), 'big')) 
    ent = int (entero1,base=2)
    global cifrado                                                   #vuelve global la variable cifrada  
    cifrado = (entero**2)%n                                          #cifra el entero convertido en binario
    #print("bin convertido a entero",entero)

a = 1
u1 = 0
b = 0
v1 = 1
 
while q1 != 0:    # este while halla los numeros de bezout para los primos escogidos
    q = p1//q1
    r = p1 - q1 * q
    u = a - q * u1
    v = b - q * v1
    #actualiza a,b
    p1 = q1
    q1 = r
    #siguiente iteracion
    a = u1
    u1 = u
    b = v1
    v1 = v

def descifrar(mensajecifrado):            #esta funcion descifra el mensaje encriptado
    ep = int((p2+1)/4)                     #generacion de a, b, r, s
    eq = int((q2+1)/4)
    r = int(mensajecifrado**(ep)%p2)
    s = int(mensajecifrado**(eq)%q2)
    x = int(((a*p2*s)+(b*q2*r))%n) 
    y = int(((a*p2*s)-(b*q2*r))%n)
    mx=(n-x)
    my=(n-y)
    
    print('Raices:',x,y,mx,my)
    if mensajecifrado == cifrado:          #condicional para que muestre el mensaje
        d1 = int(entero1, 2) 
        de1=d1.to_bytes((d1.bit_length() + 7) // 8, 'big').decode()
        print("el mensaje es: ",de1)
    else:
        print('ese no era el codigo cifrado')

if __name__ == "__main__":
    ciphertext = cifrar("hola como estas")
    cleartext = descifrar(ciphertext)
    print(ciphertext)