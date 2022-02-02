palabras=['banana','manzana','mandarina']

def traductor(palabra):
    '''Traduce a geringoso una palabra dada'''
    letras='aeiou'
    geringado=''
    
    for p in palabra:
        flag=0
        for gletra in letras:        
            if p==gletra:
                geringado+=gletra+'p'+gletra
                flag=1
        if flag==0:
            geringado+=p
                 
    return geringado

def listador(llaves):
    '''Recive una lista de palabras y luego lo recorrer generando un diccionario llamando al traductor'''
    dic={}
    for listar in llaves:
        palabra_tradu=traductor(listar)
        dic[listar]=palabra_tradu
    return dic

diccionario=listador(palabras)

print(diccionario)
