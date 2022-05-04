'''
Escribir una función que simule una calculadora científica que permita calcular el 
seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará 
al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con 
los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
'''

from math import sin, cos, tan, exp, log

def calculadora(valor, funcion):
    '''
    Definición: Esta función se encarga de aplicar la función al valor introducido
    por el usuario\n
    Parámetros de entrada:\n
    valor-->Valor al cual se le aplicará la función\n
    función-->Función seno, coseno, tangente, exponencial ó logaritmo neperiano, 
    que se le aplicará a la función\n
    Valor de retorno:\n
    La función no retorna nada. Solo muestra los valores por pantalla
    '''

    valores = range(1, valor)
    print("")
    for valor in valores:
        print("%d\t%.4f" % (valor, funcion(valor)))

numero = int(input("Por favor ingrese un número: "))
print("\nSelecciona la operación:\n1) Seno(x)\n2) Coseno(x)\n3) Tangente(x)\n4) exp(x)\n5) log(x)")
seleccion = int(input(">>: "))

if seleccion == 1:
    calculadora(numero, sin)
elif seleccion == 2:
    calculadora(numero, cos)
elif seleccion == 3:
    calculadora(numero, tan)
elif seleccion == 4:
    calculadora(numero, exp)
elif seleccion == 5:
    calculadora(numero, log)
