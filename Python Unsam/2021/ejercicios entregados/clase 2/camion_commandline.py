#CLASE 2
#Ejercicio 2.9: Funciones de la biblioteca
import csv
import sys

def costo_camion(nombre_archivo):
    '''Calulo costo camion'''
    f = open(nombre_archivo)
    rows = csv.reader(f)
    
    next(rows)    
    costo_total=0
        
    for row in rows:
        try:
            cajones=int(row[1])
            precio_c=float(row[2])
            costo_total+=cajones*precio_c
        except:
            print('Error en el proceso de datos: faltante de dato? = ',row, 'No se contabilizo la ultima linea')
   
    f.close()      
    return costo_total
    
if len(sys.argv) == 2:
    nombre_archivo=sys.argv[1]
else:
    nombre_archivo='c:/pythonej/ejercicios_python/Data/camion.csv'

costo=costo_camion(nombre_archivo)
print('Costo Total = $ ',costo)
