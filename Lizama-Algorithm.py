from Crypto.Util.number import getPrime
from random import randint
import random

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

alice['Ka'] = random.getrandbits(128)
alice['Xa'] = (p - random.getrandbits(64))
alice['Ya'] = (p - (2 * alice['Xa']) - 1)

print("Alice")
print(alice)

bob['Kb'] = random.getrandbits(128)
bob['Xb'] = (p - random.getrandbits(64))
bob['Yb'] = (p - (2 * bob['Xb']) - 1)

print("Bob")
print(bob)

# Clave publica

alice['Pa'] = mod(power_mod(g1, alice['Ka'], p) * (alice['Ka'])**2, p)
print(alice)