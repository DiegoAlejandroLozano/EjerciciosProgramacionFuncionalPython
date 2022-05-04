'''
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir 
una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y 
una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los 
productos de la cesta y devolver el precio final de la cesta.
'''

def descuento(precio, des):
    '''
    Definición: Esta función se encarga de aplicar un descuento\n 
    a un precio definido\n
    Parámetros de entrada:\n    
    precio-->Valor al cual se le aplicará el descuento\n
    desc-->Porcentaje de descuento aplicado al precio\n
    Valor retornado:\n
    precio_pagar-->Resultado de aplicar el descuento
    '''

    porcentaje = (des/100)*precio
    precio_pagar = precio - porcentaje

    return precio_pagar

def iva(precio, iva_precio):
    '''
    Definición: Esta función se encarga de aplicar el IVA al precio\n
    Parámetros de entrada:\n\n
    precio-->El precio al cual se le aplicará el IVA\n
    iva_precio-->El porcentaje de IVA a aplicar al precio\n
    Valor de rotorno:\n
    precio_pagar-->Precio real que el usuario debe pagar
    '''
    porcentaje = (iva_precio/100)*precio
    precio_pagar = precio + porcentaje

    return precio_pagar

def precio_cesta(dic_cesta, funcion):
    '''
    Definición: Esta función se encarga de aplicar los decuentos o el
    IVA a los productos de la cesta y devolver el precio final de la
    cesta\n
    Parámetros de entrada:\n
    dic_cesta-->Un diccionario que tiene los precios y los porcentajes
    de una cesta de la compra\n
    funcion-->Función encargada de aplicar descuento o el IVA\n
    Valor de retorno:\n
    precio_final-->El precio final de toda la cesta con descuento
    o con el IVA.
    '''

    sumatoria = 0
    elementos = dic_cesta.items()
    for elemento in elementos:
        sumatoria += funcion(elemento[0], elemento[1])

    return sumatoria


print("El precio de la compra tras aplicar los descuentos es: %.2f" % precio_cesta({1000:20, 500:10, 100:1}, descuento))
print("El precio de la compra tras aplicar el IVA es: %.2f" % precio_cesta({1000:20, 500:10, 100:1}, iva))
