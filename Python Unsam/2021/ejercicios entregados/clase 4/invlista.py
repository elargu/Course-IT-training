# -*- coding: utf-8 -*-

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
    lista=[1, 2, 3, 4, 5]
    lista2=['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
    
    nueva_lista1=invertir_lista(lista)
    print(f'{nueva_lista1}')
    
    nueva_lista2=invertir_lista(lista2)
    print(f'{nueva_lista2}')    
    
    return
#%%
if __name__ == "__main__":
    main()