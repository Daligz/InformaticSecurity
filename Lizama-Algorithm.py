from Crypto.Util.number import getPrime
from random import randint
import random
import hashlib

def hashKey(key):
    sha256 = hashlib.sha256()
    sha256.update(repr(key).encode())
    return sha256.hexdigest()

# Numero primo y raices primitivas | p, g1, g2

p = getPrime(128)
print("Prime: " + str(p))
g1 = primitive_root(p)
g2 = primitive_root(p)

print("g1: " + str(g1))
print("g2: " + str(g2))

# Se crean los objetos de alice y bob

alice = {}
bob = {}

# Claves privadas

print("Claves privadas")

alice['Ka'] = random.getrandbits(128)
alice['Xa'] = random.randint(1, p - 1)
alice['Ya'] = (p - (2 * alice['Xa']) - 1)

print("Alice")
print(alice)

bob['Kb'] = random.getrandbits(128)
bob['Xb'] = random.randint(1, p - 1)
bob['Yb'] = (p - (2 * bob['Xb']) - 1)

print("Bob")
print(bob)

# Clave publica

print("Claves publicas")

alice['Pa'] = mod(power_mod(g1, alice['Ka'], p) * (alice['Ka'])**2, p)
alice['Qa'] = mod(power_mod(g2, alice['Ya'], p) * alice['Ka'], p)
print("Alice")
print(alice)

bob['Pb'] = mod(power_mod(g1, bob['Kb'], p) * (bob['Kb'])**2, p)
bob['Qb'] = mod(power_mod(g2, bob['Yb'], p) * bob['Kb'], p)
print("Bob")
print(bob)

# Computo de clave secreta

print("Computo de claves secretas")

alice['Ksa'] = mod(power_mod(bob['Pb'], alice['Xa'], p) * (bob['Qb'])**alice['Ya'], p)
print("Alice")
print(alice)

bob['Ksb'] = mod(power_mod(alice['Pa'], bob['Xb'], p) * (alice['Qa'])**bob['Yb'], p)
print("Bob")
print(bob)

aliceHashKey = hashKey(alice['Ksa'])
bobHashKey = hashKey(bob['Ksb'])

print("Claves hash:")

print("Alice : " + str(aliceHashKey))
print("Bob : " + str(bobHashKey))

if (aliceHashKey == bobHashKey):
    print("Llaves correctas!")
else:
    print("Llaves incorrectas :C")