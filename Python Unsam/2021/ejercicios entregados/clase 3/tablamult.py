#solucion_de_errores.py
#Ejercicio 3.17: Tablas de multiplicar

def multi_fake(oper):
    multi=[]
    s=0
    
    for n in range(0,10):
        multi.append(s)
        s=s+oper
    
    return multi

def generador_multiplos():
    tabla=[]
    
    for n in range(0,10):
        tabla.append(multi_fake(n))
    
    return tabla

def maquetador_tabla(tabla):
    titulo=(' ','0','1','2','3','4','5','6','7','8','9')
    linea='----'
    
    print(f'{titulo[0]:>4s}{titulo[1]:>4s}{titulo[2]:>4s}{titulo[3]:>4s}{titulo[4]:>4s}{titulo[5]:>4s}{titulo[6]:>4s}{titulo[7]:>4s}{titulo[8]:>4s}{titulo[9]:>4s}')
    print(f'{linea:>4s}{linea:>4s}{linea:>4s}{linea:>4s}{linea:>4s}{linea:>4s}{linea:>4s}{linea:>4s}{linea:>4s}{linea:>4s}')
    for intera in tabla:
        print(f'{intera[0]:>3d}:{intera[1]:>4d}{intera[2]:>4d}{intera[3]:>4d}{intera[4]:>4d}{intera[5]:>4d}{intera[6]:>4d}{intera[7]:>4d}{intera[8]:>4d}{intera[9]:>4d}')
    
    return

tabla=generador_multiplos()


maquetador_tabla(tabla)

