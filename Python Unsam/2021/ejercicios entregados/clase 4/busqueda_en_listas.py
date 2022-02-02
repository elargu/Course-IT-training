# -*- coding: utf-8 -*-

#%%
#Ejercicio 4.3: Búsquedas de un elemento
#%%
def buscar_u_elemento(mi_lista, mi_elemento):
    '''
        Esta funcion busca la ultima posicion de un elemento dentro de una lista : parametros a recibir "funcion(lista,elemento)"
    '''
    rta=-1
    i=len(mi_lista)
    for ml in reversed(mi_lista):
        i-=1
        if mi_elemento == ml:
            rta=i
            break
    return rta
#%%
def buscar_n_elemento(mi_lista, mi_elemento):
    '''
        Esta funcion devuelve la cantidad de veces que aparece un elemento dentro de una lista : parametros a recibir "funcion(lista,elemento)"
    '''
    cont=0
    for ml in mi_lista:
        if mi_elemento == ml:
            cont+=1
    return cont
#%%
#Ejercicio 4.4: Búsqueda de máximo y mínimo
#%%
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    #m = 0 # Lo inicializo en 0 # LINEA CON EL PROBLEMA
    
    #Si a "m" lo inicializo en cero siempre va a ser mayor que un numero negativo. Para corregir el problema numeros negativos, la solucion es inicilizar la variable "m" con el primer elemento de la lista (suponiendo que la lista no esta vacia)
    m = lista[0]
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m
#%%
def minimo(lista):
    '''Devuelve el minimo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el minimo de los elementos a medida que recorro la lista.    
    m = lista[0]
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m
#%%
#Ejercicio 4.5: Invertir una lista
#%%
def invertir_lista(lista):
    '''
        devuelve una lista de forma invertida ej: 123 -> 321  : Parametros necesarios "funcion(lista)"
    '''
    invertida = []
    for e in lista: # Recorro la lista
        auxl=[]
        auxl.append(e)
        invertida=auxl+invertida
        
    #tambien lo podemos hacer más facil usando reversed:
# =============================================================================
#     for e in reversed(lista):
#         invertida.append(e)
# =============================================================================
        
    return invertida
#%%
def main():
    #lista=[1,2,3,2,3,4]
    #lista=[1,2,7,2,3,4]
    #lista=[1,2,3,4]
    #lista=[-5,4]
    #lista=[-5,-4]
    #lista=[32,-3,-4,63,5,91,22,24,36,-205,4,3,69,3]
    lista=[0,1,2,3,4,5,6,7,8,9]
    elemento=3
    
    posicion=buscar_u_elemento(lista, elemento)
    cantidad=buscar_n_elemento(lista, elemento)
    maxi=maximo(lista)
    mini=minimo(lista)
    inver=invertir_lista(lista)
    print(f'el elemento {elemento} esta en la posion es = {posicion} , aparece cantidad de veces n = {cantidad}')
    print(f'el maximo de la lista es = {maxi}')
    print(f'el minimo de la lista es = {mini}')
    print(f'{inver}')
    
    return
#%%
if __name__ == "__main__":
    main()