#CLASE 3
#Ejercicio 3.19: Determinar las especies en un parque

import csv
direccion_csv='c:/pythonej/ejercicios_python/Data/arbolado-en-espacios-verdes.csv'

def leer_parque(nombre_archivo, parque):
    '''Abre un csv donde esta la informacion del arbolado, realiza una busqueda de un parque especifico y devuelve en una lista un conjunto de tuplas con dicionarios de los datos de cada arbol del parque'''
    with open(nombre_archivo,'rt',encoding='utf-8') as f:
        rows=csv.reader(f)
        titulo=next(rows)
        busqueda=[]
        
        for n_row, row in enumerate(rows,start=1):
            record=dict(zip(titulo, row))
            try:
                if record['espacio_ve']==parque:
                    busqueda.append(record)
            except:
                print(f'Fila {n_row}: No puede interpretar: {row}, -dir_camiones-')
                
        return busqueda
    
def especies(lista_arboles):
        '''guardo todas las especies de arboles registrados en una plaza'''
        arboles=[]
        
        for row in lista_arboles:
            arboles.append(row['nombre_com'])
        
        tot_arboles=set(arboles)
            
        return tot_arboles

busqueda='GENERAL PAZ'
resultado=leer_parque(direccion_csv,busqueda)

print(resultado,"\n")
print(len(resultado))
print("\n")

arboles_plaza=especies(resultado)
print(arboles_plaza)
