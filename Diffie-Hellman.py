# Implementacion de la libreria secrets (https://github.com/python/cpython/blob/3.10/Lib/secrets.py)
from random import SystemRandom
randbits = SystemRandom().getrandbits

g = 2
p = 23

# No esta permitido utilizar el operador %
# Pero esta forma es muy lenta (Se utiliza pow)
def modsc(num, lim):
    n = 0
    for i in range(num):
        if (n >= lim):
            n = 0
        n += 1
    return n

def send(num, p):
    return pow(g, num, p)
    #return modsc(g ** num, p)

# Objetos para almacenar datos
alice = {}
bob = {}

# Llaves privadas
alice['xA'] = randbits(256)
bob['xB'] = randbits(256)

print(alice['xA'])
print(bob['xB'])

# Intercambio de numeros
