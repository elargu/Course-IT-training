#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################

#bibliotecas importadas#

import tkinter as tk
import sqlite3


################################################

#Funciones

def windows_precio():
	"""esta funcion es una ventana para ajustar el precio de las empanadas"""
	
	def cerrar_ventana():
		"""con esta funcion cerramos la ventana actual"""
		windows_precio.destroy()
		
	def guarda_precio():
		"""esta funcion es para guardar el precio"""
		
		while True:
			try:
				new_precio = float(box_precio.get())
				box_presuni.delete(0,tk.END)
				box_presuni.insert(0,new_precio)
				break
			except:
				box_precio.delete(0,tk.END)
				box_precio.insert(0,"ERROR")
				box_presuni.delete(0,tk.END)
				box_presuni.insert(0,"ERROR")
				break
		
	
	windows_precio = tk.Tk()
	
	windows_precio.config(width=280, height=200)
	windows_precio.title("Precio por Unidad")

	label_precio = tk.Label(windows_precio, text="Ingrese el nuevo precio     $: ")
	label_precio.place(x=20, y=50)

	box_precio = tk.Entry(windows_precio)
	box_precio.place(x=180, y=50, width=80, height=20)

	button_save = tk.Button(windows_precio, text="Guardar", command=guarda_precio)
	button_save.place(x=30, y=120, width=100, height=30)

	button_exit = tk.Button(windows_precio, text="Salir", command=cerrar_ventana)
	button_exit.place(x=150, y=120, width=100, height=30)
	
	
	
	windows_precio.mainloop()


def windows_error():
	"""ventana generica de error"""	
	
	def cerrar_ventana():
		"""esta funcion cierra la ventana actual"""
		ventana_error.destroy()

	ventana_error = tk.Tk()

	ventana_error.config(width=250, height=180)
	ventana_error.title("ERROR!")

	etiqueta_error = tk.Label(ventana_error,text="Error!: Verifique los valores ingresados.")
	etiqueta_error.place(x=25, y=50)
	#Al apretar este boton llama a la funcion de cierre de ventana
	boton_ok = tk.Button(ventana_error, text="ok", command=cerrar_ventana)
	boton_ok.place(x=75, y=100, width=100, height=30)
	
	ventana_error.mainloop()


def limpiar_pedido():
	"""esta funcion limpia el pedido de la pantalla"""
	tup = (box_relleno01, box_relleno02, box_relleno03, box_relleno04, box_relleno05, box_relleno06, box_relleno07, box_relleno08)
	for i in tup:
		i.delete(0,tk.END)
		i.insert(0,0)
	
	box_cant_totales.delete(0,tk.END)
	box_cant_totales.insert(0,0)
	
	box_total_pagar.delete(0,tk.END)
	box_total_pagar.insert(0,0.0)
	
				
def calcupedido():
	"""esta funcion calcula la cantidad totales pedidos y el precio final a pagar"""
	flag = True
	tup = (box_relleno01, box_relleno02, box_relleno03, box_relleno04, box_relleno05, box_relleno06, box_relleno07, box_relleno08)
	suma = 0
	
	try:
		punitario = float(box_presuni.get())
	except:
		box_presuni.delete(0,tk.END)
		box_presuni.insert(0,"ERROR")
		box_total_pagar.delete(0,tk.END)
		box_total_pagar.insert(0,"no hay pedido!")
		box_presuni.delete(0,tk.END)
		box_presuni.insert(0,"no hay precio!")
		windows_error()
		flag = False

	
	
	#el for es para correr y chequear el contenido de todos los cuadros
	for i in tup:
		#chequeo que haya datos enteros, de ser asi se acumulan en un sumador. De caso contrario se sobreescribe la leyenda ERROR en el cuadro que no cumple la condicion.
		try:
			boxi = int(i.get())
			suma = suma + boxi
		except:
			i.delete(0,tk.END)
			i.insert(0,"ERROR")
	#con este for verifico si hay un cuadro 'ERROR' y de ser afirmativo lanzo una ventana de error y cambio el flag a falso para no crashear el programa al calcular las cuentas.
	for i in tup:
		
		if i.get()=="ERROR":
			flag = False
			windows_error()
			break
	
	if flag == True:
		
		box_cant_totales.delete(0,tk.END)
		box_cant_totales.insert(0,suma)
	
		totalcobrar = punitario * suma
	
		#a partir de haca, estos if buscan el tipo de error en especifico y lo reemplazan con un cuadro de texto donde pertenece.
		if suma>0 and punitario>0:
			box_total_pagar.delete(0,tk.END)
			box_total_pagar.insert(0,totalcobrar)
		else:
			if suma<=0 and punitario<=0:
				box_total_pagar.delete(0,tk.END)
				box_total_pagar.insert(0,"no hay pedido!")
				box_presuni.delete(0,tk.END)
				box_presuni.insert(0,"no hay precio!")
				windows_error()
			else:
				if punitario<=0:
					box_presuni.delete(0,tk.END)
					box_presuni.insert(0,"no hay precio!")
					windows_error()
				else:
					box_total_pagar.delete(0,tk.END)
					box_total_pagar.insert(0,"no hay pedido!")
					windows_error()


def save_pedido():
	"""esta funcion es para guardar los pedidos en una base de datos"""
	tup = (box_npedido, box_relleno01, box_relleno02, box_relleno03, box_relleno04, box_relleno05, box_relleno06, box_relleno07, box_relleno08, box_cant_totales)
	tup2 = (box_presuni, box_total_pagar)
	listaa = []
	flag = True
	
	#Estos dos for son para separar los pares de los impares
	for i in tup:
		try:
			boxi = int(i.get())
			listaa.append(boxi)
		except:
			flag = False
			break
	for i in tup2:
		try:
			boxi = float(i.get())
			listaa.append(boxi)
		except:
			flag = False
			break
	#en caso de que alguno de los valores de estos box 3 se ingresen str lanzara un error.
	try:		
		boxr1 = float(box_cant_totales.get())
		boxr2 = float(box_presuni.get())
		boxr3 = float(box_total_pagar.get())
	except:
		flag = False
		windows_error()
		
	if boxr1<=0 or boxr2<=0 or boxr3<=0:
		flag = False
			
	print (listaa)
	#nos conectamos a nuestra base de datos. Con la lista que creamos pasamos los datos a la base. Chequeamos que los datos sean correctos, de contrario lanzamos una ventana de error.
	
	if flag == True:
		conn = sqlite3.connect("basedatos_ventas.sqlite.db")
		cursor = conn.cursor()
		cursor.execute("INSERT INTO pedidos VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(listaa[0],listaa[1],listaa[2],listaa[3],listaa[4],listaa[5],listaa[6],listaa[7],listaa[8],listaa[9],listaa[10],listaa[11]))

		conn.commit()
		conn.close()
	else:
		windows_error()
	
		
	numpedido()
	limpiar_pedido()
	
		
def sqlchkfila():
	"""esta funcion es para saber el numero de pedido que estamos llevando"""
	conn = sqlite3.connect("basedatos_ventas.sqlite.db")
	cursor = conn.cursor()
	
	cursor.execute("SELECT * FROM 'pedidos'")
	
	rows = cursor.fetchall()
	rows=(len(rows))
	
	conn.commit()
	conn.close()
	
	return rows

#cuando inica el programa creamos una base de datos

try:
	conn = sqlite3.connect("basedatos_ventas.sqlite.db")

	cursor = conn.cursor()
	cursor.execute("CREATE TABLE pedidos(num_pedido NUMERIC, scarsua NUMERIC, scarpican NUMERIC, sjamyque NUMERIC, sjamyroque NUMERIC, spollo NUMERIC, shumi NUMERIC, scapres NUMERIC, sespina NUMERIC, cant_totales NUMERIC, pre_unidad NUMERIC, tota_pagar NUMERIC)")

	conn.commit()
	conn.close()
except:
	None


def numpedido():
	""""con esto calculamos el numero de pedido y lo guardamos en el box"""
	try:
		box_npedido.delete(0,tk.END)
		pediahora = sqlchkfila()
		
	except:
		pediahora = 0
	box_npedido.insert(0,pediahora+1)
	

################################################
################################################

#Habilito la vetana principal

windows_principal = tk.Tk()

windows_principal.config(width=800, height=600)
windows_principal.title('Gestor Automatico de pedidos de Empanadas "REPULGATOR-3000"')


################################################

#Creo un cuadro de pedido y su etiqueta

label_npedido = tk.Label(text="Nº de Pedido")
label_npedido.place(x=10, y=35)

box_npedido = tk.Entry()
box_npedido.place(x=100, y=35, width=60, height=20)
numpedido()

#Creo dos botones para guardar o desechar lo pedido

boton_guardarp = tk.Button(text="guardar pedido", command=save_pedido)
boton_guardarp.place(x=180, y=10, width=150, height=30)

boton_desecharp = tk.Button(text="desechar pedido", command=limpiar_pedido)
boton_desecharp.place(x=180, y=50, width=150, height=30)



#Estos botones son para actualizar el precio por unidad. Si se selecciona llama a una ventan que esta en la funcion windows_precio

boton_inserprecio = tk.Button(text="actualizar precio", command=windows_precio)
boton_inserprecio.place(x=500, y=30, width=150, height=30)

label_presuni = tk.Label(text="Precio x Uni.")
label_presuni.place(x=695, y=10)

box_presuni = tk.Entry()
box_presuni.place(x=690, y=30, width=80, height=30)
box_presuni.insert(0,0)




#Etiquetas de reseña

label_subtitulo1 = tk.Label(text="TIPO DE RELLENO: ")
label_subtitulo1.place(x=100, y=100)

label_subtitulo2 = tk.Label(text="PEDIDO: ")
label_subtitulo2.place(x=300, y=100)




#Estos son las etiquetas de los sabores

label_relleno01 = tk.Label(text="Carne Suave")
label_relleno01.place(x=100, y=150)

label_relleno02 = tk.Label(text="Carne Picante")
label_relleno02.place(x=100, y=200)

label_relleno03 = tk.Label(text="Jamon y Queso")
label_relleno03.place(x=100, y=250)

label_relleno04 = tk.Label(text="Jamon y Roquefort")
label_relleno04.place(x=100, y=300)

label_relleno05 = tk.Label(text="Pollo")
label_relleno05.place(x=100, y=350)

label_relleno06 = tk.Label(text="Humita")
label_relleno06.place(x=100, y=400)

label_relleno07 = tk.Label(text="Capresse")
label_relleno07.place(x=100, y=450)

label_relleno08 = tk.Label(text="Espinaca")
label_relleno08.place(x=100, y=500)



#Estos son los cuadros de entrada de cada sabor

box_relleno01 = tk.Entry()
box_relleno01.place(x=300, y=150, width=100, height=20)
box_relleno01.insert(0,0)

box_relleno02 = tk.Entry()
box_relleno02.place(x=300, y=200, width=100, height=20)
box_relleno02.insert(0,0)

box_relleno03 = tk.Entry()
box_relleno03.place(x=300, y=250, width=100, height=20)
box_relleno03.insert(0,0)

box_relleno04 = tk.Entry()
box_relleno04.place(x=300, y=300, width=100, height=20)
box_relleno04.insert(0,0)

box_relleno05 = tk.Entry()
box_relleno05.place(x=300, y=350, width=100, height=20)
box_relleno05.insert(0,0)

box_relleno06 = tk.Entry()
box_relleno06.place(x=300, y=400, width=100, height=20)
box_relleno06.insert(0,0)

box_relleno07 = tk.Entry()
box_relleno07.place(x=300, y=450, width=100, height=20)
box_relleno07.insert(0,0)

box_relleno08 = tk.Entry()
box_relleno08.place(x=300, y=500, width=100, height=20)
box_relleno08.insert(0,0)



#Este boton, al ser apretado, calcula el pedido llamando a la funcion calcupedido

boton_calcupedido = tk.Button(text="Calcular pedido",command=calcupedido)
boton_calcupedido.place(x=540, y=350, width=200, height=50)

#en este cuadro mostramos las cantidades totales de empanadas del pedido

label_cant_totales = tk.Label(text="Cantidad totales :    ")
label_cant_totales.place(x=520, y=250)

box_cant_totales = tk.Entry()
box_cant_totales.place(x=650, y=250, width=100, height=20)
box_cant_totales.insert(0,0)

#este otro cuadro mostramos el total a pagar

label_total_pagar = tk.Label(text="Total a Pagar :          $")
label_total_pagar.place(x=520, y=300)

box_total_pagar = tk.Entry()
box_total_pagar.place(x=650, y=300, width=100, height=20)
box_total_pagar.insert(0,0.0)




################################################
################################################

windows_principal.mainloop()

################################################



###############################################
#Problemas a solucionar:

#Es posible el  ingresar datos -con intension o por equivocacion- manualmente en los siguientes box:

#box_total_pagar -flotantes
#box_cant_totales -enteros
#box_npedido -enteros
#box_presuni -flotantes

#Este problema generaria que se corrompa el correcto uso de la base de datos, incluyendo en la misma datos falsos o erroneos 

#La solucion mas logica seria el bloque de entrada de datos por parte del usuario a esos box  -opcion que estoy buscando solucionar :P


###############################################
