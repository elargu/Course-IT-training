# -*- coding: utf-8 -*-

#%%
#Ejercicio 3.18: Lectura de los árboles de un parque
#%%
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
#%%
#Ejercicio 4.15: Lectura de todos los árboles
def leer_arboles(nombre_archivo):
    #with open(nombre_archivo,'rt',encoding='utf-8') as f:
    f = open(nombre_archivo, encoding='utf-8')
    rows=csv.reader(f)
    titulo=next(rows)
    #row=next(rows)
    
    types = [float,float,int,int,int,int,int,str,str,str,str,str,str,str,str,float,float]
    posi=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #converted=[func(val) for func, val in zip(types,row)]
    #arboleda=dict(zip(titulo,converted))
    arboleda=[{ncolumna: func(row[index]) for func,ncolumna,index in zip(types,titulo,posi)}for row in rows]
    
    f.close()
    
    return arboleda

#%%
def main():
    direccion_csv='../Data/arbolado-en-espacios-verdes.csv'
    resultado=leer_arboles(direccion_csv)
    print(f'{resultado}')
    
    return
#%%
if __name__ == "__main__":
    main()