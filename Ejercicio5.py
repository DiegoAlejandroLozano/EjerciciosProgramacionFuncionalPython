'''
Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
'''

def tamaño_palabra(palabra):
    '''
    Definición: Función encargada de determinar el tamaño de las palabras\n
    Parámetros de entrada:\n
    palabra-->Palabra a la cual se le calculará su tamaño\n
    Valores retornados\n
    longitud_palabra-->Tamaño de la palabra
    '''
    longitud_palabra = len(palabra)
    return longitud_palabra

def separar_palabras(frase, funcion):
    '''
    Definición: Función encargada de separar las palabras de una frase y devolver su longitud\n
    Parámetros de entrada:\n
    frase-->Frase a la cual se le separará en palabras\n
    funcion-->Función encargada de determinar la longitud de cada palabra\n
    Valores de retorno:\n
    diccionario-->Diccionario que contiene cada palabra con su longitud
    '''
    palabras = frase.split()
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = funcion(palabra)
    return diccionario

print(separar_palabras("Welcome to Python", tamaño_palabra))