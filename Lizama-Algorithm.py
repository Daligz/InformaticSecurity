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
print()

# Se crean los objetos de alice y bob

alice = {}
bob = {}

# Claves privadas

print("Claves privadas")

alice['Ka'] = random.getrandbits(128)
alice['Xa'] = random.getrandbits(64)
alice['Ya'] = (p - (2 * alice['Xa']) - 1)

print("Alice")
print(alice)

bob['Kb'] = random.getrandbits(128)
bob['Xb'] = random.getrandbits(64)
bob['Yb'] = (p - (2 * bob['Xb']) - 1)

print("Bob")
print(bob)
print()

# Clave publica

print("Claves publicas")

alice['Pa'] = mod((power_mod(g1, alice['Xa'], p)) * (power_mod(alice['Ka'], 2, p)), p)
alice['Qa'] = mod((power_mod(g2, alice['Ya'], p)) * mod(alice['Ka'], p), p)
print("Alice")
print(alice)

bob['Pb'] = mod((power_mod(g1, bob['Xb'], p)) * (power_mod(bob['Kb'], 2, p)), p)
bob['Qb'] = mod((power_mod(g2, bob['Yb'], p)) * mod(bob['Kb'], p), p)
print("Bob")
print(bob)
print()

# Computo de clave secreta

print("Computo de claves secretas")

alice['Ksa'] = mod(power_mod(bob['Pb'], alice['Xa'], p) * power_mod(bob['Qb'], alice['Ya'], p), p)
print("Alice")
print(alice)

bob['Ksb'] = mod(power_mod(alice['Pa'], bob['Xb'], p) * power_mod(alice['Qa'], bob['Yb'], p), p)
print("Bob")
print(bob)
print()

aliceHashKey = hashKey(alice['Ksa'])
bobHashKey = hashKey(bob['Ksb'])

print("Claves hash:")

print("Alice : " + str(aliceHashKey))
print("Bob : " + str(bobHashKey))
print()

if (aliceHashKey == bobHashKey):
    print("Llaves correctas!")
else:
    print("Llaves incorrectas :C")