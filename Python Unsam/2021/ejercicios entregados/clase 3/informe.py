#Clase 3
#Ejercicio 3.9: La función zip()

import csv
dir_camiones='c:/pythonej/ejercicios_python/Data/fecha_camion.csv'
dir_precios='c:/pythonej/ejercicios_python/Data/precios.csv'

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    total = 0.0
    camion=[]
    
    with open(nombre_archivo,'rt') as f:
        rows=csv.reader(f)
        titulo=next(rows)
        
        for n_row, row in enumerate(rows,start=1):
            record=dict(zip(titulo, row))
            try:
                record['cajones']=int(record['cajones'])
                record['precio']=float(record['precio'])
                camion.append(record)
            except ValueError:
                print(f'Fila {n_row}: No puede interpretar: {row}')
   
    return camion

def leer_precios(nombre_archivo):
    '''Lee una lista de precios desde un archivo csv y los guarda como diccionario'''
    f=open(nombre_archivo,'r')
    rows=csv.reader(f)
    diccionario={}
    
    for n_row,row in enumerate(rows, start=1):
        try:
            diccionario[row[0]]=float(row[1])
        except:
            print(f'Fila {n_row}: No puede interpretar: {row} - dir_precio-')
    f.close()
    
    return diccionario

def costo_camion(dic):
    '''calcula el costo del camion usando un diccionario'''
    total=0.0
    
    for n_clave,clave in enumerate(dic, start=1):
        try:
            total+=clave['cajones']*clave['precio']
        except:
            print(f'Fila {n_clave}: No puede interpretar: {clave}, -dir_camiones-')
    
    return total

def calculo_venta(dic_precio,camion):
    '''Calcula la venta usando el diccionario con los precios y el contenido del camion'''
    total_venta=0.0
    
    dic_camion=camion    #guarda la lista con los diccionarios del camion en una variable
    p=dic_precio
    
    for n_c, c in enumerate(dic_camion, start=1):
          try:
            if p[c['nombre']]!=0:
                total_venta+=c['cajones'] * p[c['nombre']]
          except:
             print(f'Fila {n_c}: No puede interpretar: {c} - dir_camion o dir_precios-')
           
    return total_venta

def ganancias(dif):
    '''Verifico Ganancias'''
    if diferencia>0:
        print('Hubo GANANCIA')
    elif diferencia<0:
        print('Hubo PERDIDA')
    else:
        print('Empate a cero')
    return

mi_camion=leer_camion(dir_camiones)
diccio=leer_precios(dir_precios)

venta=calculo_venta(diccio,mi_camion)
print('Total Venta : $ ',venta)

costo_total=costo_camion(mi_camion)
print('Costo camion : $ ',costo_total)

diferencia=venta-costo_total
print('diferencia: $ ',f'{diferencia:0.2f}')

ganancias(diferencia)
