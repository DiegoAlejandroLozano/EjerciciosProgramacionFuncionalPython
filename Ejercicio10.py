'''Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá 
como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual 
que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del 
inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5'''

def precio_inmueble(antiguegad, num_metros, num_habitaciones, garaje, tipo_zona):
    '''Definición: Función encargada de determinar el precio del inmueble, en función de la zona en el que se encuentra ubicado\n
    Parámetros de entrada:\n
    antiguedad-->año del inmueble\n
    num_metros-->número de metros del inmueble\n
    num_habitaciones-->número de habitaciones del inmueble\n
    garaje-->indica si el inmueble tiene o no garaje\n
    tipo_zona-->tipo de zona a la que pertenece el inmueble\n
    Valores de Retorno:\n
    precio-->Valor del inmueble'''

    precio = 0

    if tipo_zona == 'A':
        precio = (num_metros * 1000 + num_habitaciones * 5000 + int(garaje) * 15000) * (1-(2020-antiguegad) / 100) 
    elif tipo_zona == 'B':
        precio = (num_metros * 1000 + num_habitaciones * 5000 + int(garaje) * 15000) * (1-(2020-antiguegad) / 100) * 1.5

    return precio

def realizar_busqueda(lista_inmuebles, precio):
    '''Definición: Función encargada de buscar el tipo del inmueble, en función  del precio proporcionado\n
    Parámetros de entrada:\n
    lista_inmuebles-->Lista con todos los inmuebles disponibles\n
    precio-->Precio del inmueble buscado\n
    Valores de retorno:\n
    lista_inmuebles_aprobados-->Lista que contiene todos los inmuebles aprobados
    '''

    lista_inmuebles_aprobados = []
    
    for inmueble in lista_inmuebles:
        p_inmueble = precio_inmueble(inmueble['año'], inmueble['metros'], inmueble['habitaciones'], inmueble['garaje'], inmueble['zona'])
        if p_inmueble <= precio:
            inmueble["precio"] = p_inmueble
            lista_inmuebles_aprobados.append(inmueble)

    return lista_inmuebles_aprobados


inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

print(realizar_busqueda(inmuebles, 150000))