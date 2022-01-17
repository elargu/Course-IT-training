#!/usr/bin/env python
# -*- coding: utf-8 -*-
#importo tkinter
import tkinter as tk
#armo funciones


def numuno():
	cajauno.insert(tk.END,1)

def numdos():
	cajauno.insert(tk.END,2)
	
def numtres():
	cajauno.insert(tk.END,3)

def numcuatro():
	cajauno.insert(tk.END,4)
	
def numcinco():
	cajauno.insert(tk.END,5)
	
def numseis():
	cajauno.insert(tk.END,6)

def numsiete():
	cajauno.insert(tk.END,7)
	
def numocho():
	cajauno.insert(tk.END,8)
	
def numnueve():
	cajauno.insert(tk.END,9)

def numcero():
	cajauno.insert(tk.END,0)

def botigual():
	a=cajauno.get()
	try:
		a=str(eval(a))
	except:
		a="error"
	cajauno.delete(0,tk.END)
	cajauno.insert(tk.END,a)
	
def botpunto():
	cajauno.insert(tk.END,".")

def botnega():
	cajauno.insert(0,"-")
	
def botmas():
	cajauno.insert(tk.END,"+")
	
def botmenos():
	cajauno.insert(tk.END,"-")

def botpor():
	cajauno.insert(tk.END,"*")
	
def botdivi():
	cajauno.insert(tk.END,"/")
	
def botpoten():
	cajauno.insert(tk.END,"^")

def botdel():
	cajauno.delete(0,tk.END)
	

def suma():
	#con la primera linea borro la caja si tiene informacion
	cajatres.delete(0,tk.END)
	#capturo la informacion de la caja 1 y 2
	a=cajauno.get()
	b=cajados.get()
	#lo paso a entero
	a=int(a)
	b=int(b)
	#hago la ecucacion
	c=a+b
	#pego en la caja 3 la informacion que esta en la variable "c", el 0 que figura es la posicion adentro de la caja donde aparecera el resultado
	cajatres.insert(0,c)

def resta():
	cajatres.delete(0,tk.END)
	a=cajauno.get()
	b=cajados.get()
	a=int(a)
	b=int(b)
	c=a-b
	cajatres.insert(0,c)

def multi():
	cajatres.delete(0,tk.END)
	a=cajauno.get()
	b=cajados.get()
	a=int(a)
	b=int(b)
	c=a*b
	cajatres.insert(0,c)


def divi():
	cajatres.delete(0,tk.END)
	a=cajauno.get()
	b=cajados.get()
	a=int(a)
	b=int(b)
	if b!=0:
		c=a/b
		cajatres.insert(0,c)
	else:
		cajatres.insert(0,"error, no cero div")


#importo una ventana
ventana = tk.Tk()

#configuro la ventana y le pongo titulo
ventana.config(width=320, height=300)
ventana.title("Calculadora")

##############################################


cajauno = tk.Entry()
cajauno.place(x=10,y=10, width=300, height=40)


###############################################


butonuno=tk.Button(text=" 1 ", command = numuno)
butonuno.place(x=10,y=60, width=60, height=50)

butondos=tk.Button(text=" 2 ", command = numdos)
butondos.place(x=70,y=60, width=60, height=50)

butontres=tk.Button(text=" 3 ", command = numtres)
butontres.place(x=130,y=60, width=60, height=50)

butoncuatro=tk.Button(text=" 4 ", command = numcuatro)
butoncuatro.place(x=10,y=110, width=60, height=50)

butoncinco=tk.Button(text=" 5 ", command = numcinco)
butoncinco.place(x=70,y=110, width=60, height=50)

butonseis=tk.Button(text=" 6 ", command = numseis)
butonseis.place(x=130,y=110, width=60, height=50)

butonsiete=tk.Button(text=" 7 ", command = numsiete)
butonsiete.place(x=10,y=160, width=60, height=50)

butonocho=tk.Button(text=" 8 ", command = numocho)
butonocho.place(x=70,y=160, width=60, height=50)

butonnueve=tk.Button(text=" 9 ", command = numnueve)
butonnueve.place(x=130,y=160, width=60, height=50)

butonnegativo=tk.Button(text=" +/- ", command = botnega)
butonnegativo.place(x=10,y=210, width=60, height=50)

butoncero=tk.Button(text=" 0 ", command = numcero)
butoncero.place(x=70,y=210, width=60, height=50)

butonpunto=tk.Button(text=" . ", command = botpunto)
butonpunto.place(x=130,y=210, width=60, height=50)

butonsum=tk.Button(text=" + ", command = botmas)
butonsum.place(x=190,y=60, width=60, height=100)

butonres=tk.Button(text=" - ", command = botmenos)
butonres.place(x=190,y=160, width=60, height=50)

butonigual=tk.Button(text=" = ", command = botigual)
butonigual.place(x=190,y=210, width=60, height=50)

butonigual=tk.Button(text=" DEL ", command = botdel)
butonigual.place(x=250,y=210, width=60, height=50)

butonmult=tk.Button(text=" x ", command = botpor)
butonmult.place(x=250,y=60, width=60, height=50)

butondivi=tk.Button(text=" / ", command = botdivi)
butondivi.place(x=250,y=110, width=60, height=50)

butonpotencia=tk.Button(text=" X^X ", command = botpoten)
butonpotencia.place(x=250,y=160, width=60, height=50)



################################################






"""etiqueta=tk.Label(text="ingrese dos numeros:")
etiqueta.place(x=20,y=90)

etiqueta=tk.Label(text="Resultado:")
etiqueta.place(x=20,y=150)"""

ventana.mainloop()
