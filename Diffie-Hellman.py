import hashlib
# Implementacion de la libreria secrets (https://github.com/python/cpython/blob/3.10/Lib/secrets.py)
from random import SystemRandom
randbits = SystemRandom().getrandbits

g = 2
# En hexadecimal
#p = 23

# Para garantizar la seguridad, se recomienda que el número primo (p) tenga al menos 2048 bits de longitud,
# que es el equivalente binario de un número decimal de aproximadamente este tamaño:
p = 41536875762873659842593824756984376582763487912837582736592873684273684728938572983759283475934875938475928475928739587249587298739587298357928759827958375298763482736857298435793487958279385792873954877239759283759247859386704598679238473782673526735476235687348693869456734568276594980638490248758096039479027945982730187439759284620950293759287049502938058920983945872094860298491283750294801937109248019358103799581093750193850791395710937597019385089103951073058710393701934701938091803984091804981093801985013984019835091835019830910791803958103951903951809358109385019840193580193840198340918093851098309180019

# No esta permitido utilizar el operador %
# Pero esta forma es muy lenta (Se utiliza pow)
def modsc(num, lim):
    n = 0
    for i in range(num):
        if (n >= lim):
            n = 0
        n += 1
    return n

# Otra implementacion del modulo
# Pero no esta probado
def modscv2(num, lim):
    if (num > lim):
        num -= lim
        return modscv2(num, lim)
    return num

# Comprobar numeros no permitidos
banned = [0]
def getRandom256():
    rand = randbits(256)
    while (rand in banned):
        rand = randbits(256)
    return rand

def hashKey(key):
    sha256 = hashlib.sha256()
    sha256.update(repr(key).encode())
    return sha256.hexdigest()

# Objetos para almacenar datos
alice = {}
bob = {}

# Llaves privadas
alice['xA'] = getRandom256()
bob['xB'] = getRandom256()

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