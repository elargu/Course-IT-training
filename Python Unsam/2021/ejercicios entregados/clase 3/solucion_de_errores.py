#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: Tiene dos errores, el primero es que el if solo valida si la 'a' es minuscula y no reconocelas 'A' mayuscula (error semantico). El segundo problema esta en el ciclo while, cuando uno quiere verificar si existe una 'a' o 'A' solo guarda la comparacion de la primera letra que verifico ya que el return esta dentro del if (error semantico)
#    Lo corregí agregando en el if un or 'A' (para que reconozca la mayuscula).
#    Lo corregí agregando una variable inicializada con False que guarde el resultado en caso de encontrar la letra, la misma variable es la que se devuelve en el return. Ya no es necesario tener un else.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    resultado=False
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            resultado=True
        i += 1
    return resultado
    
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Hay varios errores, los errores de sintaxis estan en que faltan los ':' al declarar la funcion, el while y el if. Luego el return "Falso" no existe, es "False" (error de sintaxis). Tambien en el if la comparacion se hace con un solo = y se debe usar dos ==. (error de sintaxis)  Ademas sigue arrastrando el mismo error semantico que en el ejercicio anteior, no reconoce las 'A' mayusculas. 
#    Lo corregí agregando los ':' al final de la declaracion del def, del while y del if. Al return lo cambie por False y finalmente le modifique el if para que reconozca las 'A' con un or ademas de comparar con un '=='
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False
    
tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: Hay un Error en Tiempo de Ejecucion en a entrada '1984' que es un numero entero y no es un objeto que se pueda interar como una cadena o un string. Lo ideal seria casterlo a str y luego pasarlo por len.
#...Lo corregí agregando un casteo al principio de la funcion, reconvierto la variable en string
#    A continuación va el código corregido
def tiene_uno(expresion):
    expresion=str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
#Ejercicio 3.4. Función suma(a,b)
#Comentario: Es un Error de semantico, el error era que en la funcion no tenia retorno 'Return', no se devolvia ningun resultado o variable. El c de adentro de la funcion era una variable local.
#...Lo corregí agregando un Return de la variable local c
#    A continuación va el código corregido
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5. Función leer_camion(nombre_archivo)
#Comentario: Es un Error Semantico, el problema es que en cada interacion del ciclo for estoy pisando el diccionario 'registro'.
#...Se soluciona moviendo la declaracion del diccionario registro={} adentro del ciclo for cuando comienza
#    A continuación va el código corregido

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('c:/pythonej/ejercicios_python/Data/camion.csv')
pprint(camion)