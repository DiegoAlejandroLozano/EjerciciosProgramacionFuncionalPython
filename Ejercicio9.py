'''Escribir una función que calcule el módulo de un vector.'''

from math import sqrt

def modulo_vector(x,y, z=0):
    modulo = sqrt( (x**2) + (y**2) + (z**2) )
    return modulo

print(modulo_vector(3, 4))
print(modulo_vector(1,2,3))