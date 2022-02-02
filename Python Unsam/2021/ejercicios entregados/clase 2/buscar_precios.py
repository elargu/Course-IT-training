#Clase 2
#Ejercicio 2.7: Buscar precios
#Ejercicio 2.8: Administración de errores

def buscar_precio(fruta):
    '''La funcion busca el precio segun un criterio de busqueda ingresado por el usuario'''
    for line in f:
        row=line.split(',')
        if row[0] == search:
            precio_fruta=float(row[1])

    try:
        return precio_fruta
    except:
        print(fruta,'no figura en el listado de precios')
    
        


f=open('c:/pythonej/ejercicios_python/Data/precios.csv','rt')

search=input('ingrese fruta: ')
busquedaok=buscar_precio(search)

if type(busquedaok)==float:
    print('El precio de un cajon de ',search,' es = $ ',busquedaok)

f.close()



