'''
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
'''

def  calificación(nota):
    '''Definición: Función encargada de asignar la calificacióin, según la nota\n
    Parámetros de entrada:\n
    nota-->nota a la cual se le asignara la calificación\n
    Valores de retorno\n
    Reprobado-->Calificación obtenida si la nota es menor de 3\n
    Aprobado-->Calificación obtenida si la nota es mayor de 3'''

    if nota < 3:
        return "Reprobado"
    elif nota >= 3:
        return "Aprobado"


def procesar_calificación(dic_notas, función):
    '''Definición: Función encargada de pasar las materias a mayusculas y asignar tu calificación según la nota\n
    Parámetros de entrada:\n
    dic_notas-->Contiene la asignaturas y las notas correspondientes a un alumno\n
    funcion-->Función encargada de asignar la calificación, según la nota\n
    Valores de retorno\n
    calificaciones-->Diccionario con las asignaturas en mayusculas y con las calificaciones'''
    
    notas = dic_notas.items()
    calificaciones = {}
    
    for nota in notas:
        calificaciones[nota[0].upper()] = función(nota[1])
    
    return calificaciones


asignaturas_notas = {'física':5, 'matemáticas':5, 'lenguaje':2.9, 'química':4.5, 'filosofía':1.5}

print(procesar_calificación(asignaturas_notas, calificación))