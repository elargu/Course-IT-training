#!/usr/bin/env python
# -*- coding: utf-8 -*-

azucar=[35,55,60,30]

#inicio i y una bandera en caso de que no haya algun supermercado con precio menor a 40

i=0
flag=False

#hago un ciclo para que revice los precios, leo con lent el tamaño del array

while i<=((len(azucar))-1):
	#pongo un condicional, si el precio coincide con el criterio se imprime el numero del supermercado y la bandera cambia a verdadero para saltear un mensaje de respuesta negativa.
	if azucar[i]<40:
		print("supermercado N° ",i+1)
		flag=True
	i=i+1

#si no hay ningun dato que coincida con el criterio del primer if, creo otro para que me muestre un mensaje negativo.

if flag==False:
	print("no hay supermercados con azucar de precio menor a $ 40")
