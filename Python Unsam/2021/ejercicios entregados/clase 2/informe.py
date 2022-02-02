#Clase 2
#Ejercicio 2.16: Lista de diccionarios

import csv
dir_camiones='c:/pythonej/ejercicios_python/Data/camion.csv'
dir_precios='c:/pythonej/ejercicios_python/Data/precios.csv'


def camion_diccio(archivo):
    '''lee el archivo camion.csv y guarda en una lista diccionarios que describen el contenido del camion'''
    camion=[]
    respuesta=[]
    
    with open(archivo,'rt') as f:
        rows=csv.reader(f)
        titulo=next(rows)
        for row in rows:
            lote={}
            lote[titulo[0]]=row[0]
            lote[titulo[1]]=int(row[1])
            lote[titulo[2]]=float(row[2])
            camion.append(lote)
    respuesta=[camion,titulo]
    return respuesta

def costo_camion(paquete):
    '''calcula el costo del camion usando un paquete que tiene el diccionario y sus claves'''
    total=0.0
    
    #en dic se desempaqueta la lista con los diccionarios
    dic=paquete[0]
    #en cada variable se desempaquetan las claves que tengo que utilizar: clave_a='cajones' , clave_b='precio'
    clave_a=paquete[1][1]
    clave_b=paquete[1][2]
    
    for clave in dic:
        total+=clave[clave_a]*clave[clave_b]
    
    return total

def leer_precios(archi):
    '''Lee una lista de precios desde un archivo csv y los guarda como diccionario'''
    import csv
    f=open(archi,'r')
    rows=csv.reader(f)
    diccionario={}
    
    for row in rows:
        try:
            diccionario[row[0]]=float(row[1])
        except:
            print('hubo un error en el contenido del archivo?!, un dato no fue guardado = ref.data{ ',row,' }')
    return diccionario

def calculo_venta(dic_precio,camion):
    '''Calcula la venta usando el diccionario con los precios y el contenido del camion'''
    total_venta=0.0
    
    dic_camion=camion[0]    #guarda la lista con los diccionarios del camion en una variable
    clave_a=camion[1][0]    #guarda el nombre clave_a='nombre'
    clave_b=camion[1][1]    #guarda el nombre clave_a='cajones'
    p=dic_precio
    
    for c in dic_camion:
          if p[c[clave_a]]!=0:
            total_venta+=c[clave_b] * p[c[clave_a]]
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


mi_camion=camion_diccio(dir_camiones)
diccio=leer_precios(dir_precios)

venta=calculo_venta(diccio,mi_camion)
print('Total Venta : $ ',venta)

costo_total=costo_camion(mi_camion)
print('Costo camion : $ ',costo_total)

diferencia=venta-costo_total
print('diferencia: $ ',f'{diferencia:0.2f}')

ganancias(diferencia)

