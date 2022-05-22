# Implementacion de la libreria secrets (https://github.com/python/cpython/blob/3.10/Lib/secrets.py)
from random import SystemRandom
_sysrand = SystemRandom()

randbits = _sysrand.getrandbits

g = 2
p = 23

def modsc(num, lim):
    n = 0
    for i in range(num):
        if (n >= lim):
            n = 0
        n += 1
    return n

def send(p, num):
    return modsc(g ** num, p)

print(send(p, 6)) # 8
print(randbits(256))