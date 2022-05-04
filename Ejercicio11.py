'''Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya 
puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene restando la media 
y dividiendo por la desviación típica de la muestra.'''

from math import sqrt

def puntuación_típica(valor, media, desviación_típica):
    '''Definición: Función encargada de determinar la puntuación típica de un valor\n
    Parámetros de entrada:\n
    valor-->Valor al cual se le calculará la puntuación típica\n
    media-->Media arimética\n
    desviación_típica-->Desviación típica\n
    Valores de retorno:\n
    puntuación--> Puntuación típica del valor'''

    puntuación = ( valor - media ) / desviación_típica
    return puntuación

def valores_atípicos(lista_valores, _f_puntuación_típica):
    '''Definición: Función encargada de determinar los valores atípicos de una lista de valores\n
    Parámetros de entrada:\n
    lista_valores-->Valores a los cuales se les calculará los valores atípicos\n
    _p_puntuación_típica--> Función encargada de calcular la puntuación típica\n
    Valores de retorno:\n
    lista_valores_atípicos--> Lista con los valores atípicos encontrados'''

    #Calculando la media
    sum1 = 0
    for valor in lista_valores:
        sum1 += valor
    media = sum1 / len(lista_valores)

    #Calculando la desviación típica
    sum2 = 0
    for valor in lista_valores:
        sum2 += (valor - media)**2
    desviacion = sqrt( sum2 / ( len(lista_valores) - 1 ) )

    #Determinando los valores atípicos
    lista_valores_atípicos = []

    for valor in lista_valores:
        if _f_puntuación_típica(valor, media, desviacion) > 3 or _f_puntuación_típica(valor, media, desviacion) < -3:
            lista_valores_atípicos.append(valor)

    return lista_valores_atípicos

print(valores_atípicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000], puntuación_típica))
