from Crypto.Util.number import getPrime
from random import randint
import random

def getNumCondition(n):
    rand = random.getrandbits(1024)
    if (rand < 0 | rand > n):
        return getNumCondition(n)
    return rand

def inverse(num, pown, n):
    return power_mod(inverse_mod(num, n), pown, n)

p = getPrime(1024)
n = p
y = getNumCondition(n)

print("p: " + str(p))
print("n: " + str(n))
print("y: " + str(y))

data = {}
channel = {}

data['Pa1'] = power_mod(y, 2, n)
data['Pa2'] = power_mod(y, 3, n)
data['Pa3'] = power_mod(y, 5, n)
data['Ra'] = power_mod(y, 1, n)

m = getNumCondition(n)

channel['Ca1'] = power_mod((y * m) + inverse(y, 1, n), 2, n)
channel['Ca2'] = power_mod((pow(y, 2) * m) + inverse(y, 1, n), 3, n)
channel['Ca3'] = power_mod((pow(y, 3) * m) + inverse(y, 2, n), 5, n)

channel['Cr1'] = power_mod(pow(y, 2) * pow(m, 2) + 2 * m + inverse(y, 2, n), 1, n)
channel['Cr2'] = power_mod(pow(y, 6) * pow(m, 3) + (3 * pow(y, 3)) * pow(m, 2) + 3 * m + inverse(y, 3, n), 1, n)
channel['Cr3'] = power_mod(pow(y, 15) * pow(m, 5) + (5 * pow(y, 10) * pow(m, 4)) + (10 * pow(y, 5) * pow(m, 3)) + (10 * pow(m, 2)) + (5 * inverse(y, 5, n) * m) + inverse(y, 10, n), 1, n)

def check(fNum, sNum):
    if (fNum == sNum):
        print("Los resultados son iguales!")
    else:
        print("Los resultados no son iguales :c")

print("")
print("Escenario 1")
check(channel['Ca1'], channel['Cr1'])

print("")
print("Escenario 2")
check(channel['Ca2'], channel['Cr2'])

print("")
print("Escenario 3")
check(channel['Ca3'], channel['Cr3'])