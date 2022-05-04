'''
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
'''

def calificación_nota(nota):
    '''Definición: Función encargada de designar la calificación, según la nota\n
    Parámetros de entrada:\n
    nota-->La nota correspondiente, la cual será evaluada\n
    Valores de retorno\n
    Reprobado--> Valor asignado a notas inferiores a 3\n
    Aprobado--> Valor asignado a notas entre 3 y menores a 4\n
    Excelente--> Valor asignado a notas superiores o iguales a 4'''

    calificación = 0

    if nota < 3:
        return "Reprobado"
    elif nota >= 3 and nota < 4:
        return "Aprobado"
    elif nota >= 4:
        return "Excelente"

def calificaciones(lista_notas, función):
    '''Definición: Función encargada de terminar la calificación de un grupo de notas\n
    Parámetros de entrada:\n
    lista_notas-->Lista de notas, las cuales serán evaluadas\n
    función-->Función encargada de evaluar la calificación, según la nota\n
    Valores devueltos:\n
    resultado-->Contiene una lista con todas las calificaciones'''
    
    resultado = []

    for  nota in lista_notas:
        resultado.append(función(nota))
    return resultado


print(calificaciones([1, 5, 3.5, 4, 4.1, 2.9], calificación_nota))

