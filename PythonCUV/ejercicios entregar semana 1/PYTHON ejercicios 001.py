#!/usr/bin/env python
# -*- coding: utf-8 -*-

#le pido al usuario que ingrese los datos

print("Este programa le informara cual es el precio final de un producto con un precio sin iva.")
producto = input("ingrese nombre del producto: ")
precio = input("ingrese el precio bruto: ")

#convierto el dato ingresado "precio" de str a float

precio = float(precio)

#proceso los datos

precio = precio*1.21

#doy la salida del resultado

print("el precio con iva de ",producto," es $ ",precio)

