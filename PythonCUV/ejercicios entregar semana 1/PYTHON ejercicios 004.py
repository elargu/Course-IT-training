#!/usr/bin/env python
# -*- coding: utf-8 -*-

#introduccion
print("vamos a calcular el area de un circulo")
#le pido una unidad, es solo estetico para ponerlo en el resultado.
unidt=input("ingrese en que unidad de medida va a trabajar mts,cm,mm: ")

#importo la funcion math, asigno pi a una variable y lo paso a float
import math
pi=float(format(math.pi))

#inicio rad en cero para que inicie el bucle while
rad="0"

#este bucle lo hice para validar una respuesta. Si el usuario ingresa el dato en diametro o en radio.
while rad!="1" and rad!="2":
	rad=input("ingrese si va a trabajar con radio o diametro, para diametro ingrese 1, para radio ingrese 2: ")
	if rad!="1" and rad!="2":
		print("el comando ingresado no es correcto. Ingrese 1 para diametro, 2 para radio.")

#dependiendo de si el dato ingresado es diametro o radio armo un if para los dos caminos. Si es diametro se divide por 2. Antes pasamos todo a float.
if rad=="1":
	rad=input("ingrese el diametro: ")
	rad=float(rad)
	rad=rad/2
else:
	rad=input("ingrese el radio: ")
	rad=float(rad)

#proceso el dato
rad=pi*(rad**2)
#imprimo el resultado
print("el area del circulo es: ",rad," ",unidt,"ᶺ2")
			
