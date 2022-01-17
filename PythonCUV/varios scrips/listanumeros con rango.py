#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
def un_rango(desde_X, hasta_Y):
	lista_rango = []
	for i in range(desde_X, hasta_Y):
		lista_rango.append(i)
	return lista_rango

a = int(input("ingrese rango inicio"))
b = int(input("ingrese rango final, no incluido"))

lista_num = un_rango(a, b)
print(lista_num)
