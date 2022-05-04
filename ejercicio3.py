'''
Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
'''

def cuadrado(x):
    '''
    Definición: Función encargada de elevar al cuadrado el valor de x\n
    Parámetros de entrada:\n
    x--> Valor el cual se elevará al cuadrado\n
    Valor de retorno:\n
    cuadrado--> El resultado de elevar al cuadrado el número
    '''

    cuadrado = x**2
    return cuadrado

def modificar(lista, funcion):
    '''
    Definición: Función encargada de aplicar una función a 
    todos los elementos de una lista.\n
    Parámetros de entrada:\n
    lista--> Lista de valores a modificar\n
    funcion--> Función que se aplicará a todos los elementos de la lista\n
    Valores de retorno:\n
    lista_modificada--> Lista con los valores modificados
    '''

    lista_modificada = []
    for elemento in lista:
        lista_modificada.append(funcion(elemento))

    return lista_modificada

lista_valores = [1, 2, 3, 4]
print(list(lista_valores))
print(modificar(lista_valores, cuadrado))

