#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
def pelis(a,b,c):
	j=0
	for i in a:
		print(i, b[j], c[j])
		j=j+1



lista_pelicula = ["Duro de Matar", "Locademia de policia", "La Pistola Desnuda"]
lista_anio = [1989, 1990, 1994]
lista_genero = ["Accion", "Comedia", "Comedia"]

pelis(lista_pelicula,lista_anio,lista_genero)
