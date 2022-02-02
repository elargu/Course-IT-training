# -*- coding: utf-8 -*-

#%%
#Ejercicio 4.6: Propagación
#%%
def propagar(vector):
    '''
        Reciba un vector con 0's, 1's y -1's y devuelva como salida otro vector en el que los 1's se propagaron a sus vecinos con 0
    '''
    on_fire=vector.copy()    
    tam=len(vector)
   
    #recorro la lista atras hacia adelante, para propagar los 1 de la derecha
    for i,fosforo in enumerate(on_fire):
        if fosforo==1:
            if i<tam-1:
                if on_fire[i+1]==0:
                    on_fire[i+1]=1
    
    #luego uso otro for para propagar los 1 que se acaban de encender en la lista anterior y si es que existe un cero tras de el. Se lista al reves.
    i=tam
    for fosforo in reversed(on_fire):
        i-=1
        if fosforo==1:
            if i>0:
                if on_fire[i-1]==0:
                    on_fire[i-1]=1
     #finalmente devulvo el resultado en una nueva lista (no piso la anterior)   
    return on_fire
    
#%%
def main():
    
    vector=[0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
    #vector=[ 0, 0, 0, 1, 0, 0]

    quemados=propagar(vector)
    print(vector)
    print(f'{quemados}')

    return

#%%
if __name__ == "__main__":
    main()