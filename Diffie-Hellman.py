import hashlib
# Implementacion de la libreria secrets (https://github.com/python/cpython/blob/3.10/Lib/secrets.py)
from random import SystemRandom
from turtle import st
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

def hashKey(key):
    sha256 = hashlib.sha256()
    sha256.update(repr(key).encode())
    return sha256.hexdigest()

# Objetos para almacenar datos
alice = {}
bob = {}

# Llaves privadas
alice['xA'] = randbits(256)
bob['xB'] = randbits(256)

print("Llaves privadas:")
print("Bob: " + str(bob['xB']))
print("Alice: " + str(alice['xA']))
print()

# Intercambio de numeros
bob['cA'] = pow(g, alice['xA'], p)
alice['cB'] = pow(g, bob['xB'], p) 

# Computo de llave secreta
bob['Kba'] = pow(bob['cA'], bob['xB'], p)
alice['Kab'] = pow(alice['cB'], alice['xA'], p)

print("Claves:")
print("Bob : " + str(bob['Kba']))
print("Alice : " + str(alice['Kab']))
print()

bobHashKey = hashKey(bob['Kba'])
aliceHashKey = hashKey(alice['Kab'])

print("Claves hash:")
print("Bob : " + str(bobHashKey))
print("Alice : " + str(aliceHashKey))
print()

if (bobHashKey == aliceHashKey):
    print("Llaves correctas!")
else:
    print("Llaves incorrectas :C")