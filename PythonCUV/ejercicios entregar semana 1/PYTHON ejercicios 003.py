#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("vamos a calcular el area de un triangulo")
unidt=input("ingrese en que unidad de medida va a trabajar mts,cm,mm : ")

#le pido al usuario que ingrese la base y lo pasamos a real"
baset=input("ingrese base del triangulo: ")
baset=float(baset)

#le pido al usuario que ingrese la altura y tambien la pasamos a real"
alturat=input("ingrese altura del triangulo: ")
alturat=float(alturat)

#calculo el area y la guaro en la variable "baset"
baset=(baset*alturat)/2

#de salida imprimo el resultado
print("el area del triangulo es: ",baset," ",unidt,"ᶺ2")
