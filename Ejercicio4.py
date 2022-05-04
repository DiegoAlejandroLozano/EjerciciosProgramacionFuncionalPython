'''
Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.
'''

def funcion_booleana(numero):
    """
    Definición: Función encargada de determinar si un número es divisible por 3\n
    Parámetros de entrada:\n
    numero--> Número a evaluar\n
    Valor de retorno:\n
    La función retorna True si el número es divisible por tres. En caso contrario,
    la función devuelve False.
    """
    return (numero%3)==0

def filtro(lista,funcion):
    '''
    Definición: Esta función crea una nueva lista, como resultado de aplicar la función\n
    Parámetros de entrada:\n
    lista--> Lista de números a evaluar.\n
    funcion--> Función que se le aplicará a los elementos de la lista\n
    Valor de retorno:\n
    resultado-->Resultado de aplicar la función  a la lista.
    '''
    resultado = []
    for elemento in lista:
        if funcion(elemento):
            resultado.append(elemento)
    return resultado

print(filtro(range(100),funcion_booleana))