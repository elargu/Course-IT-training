#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sqlchkfila():
	
	conn = sqlite3.connect("basedatos_ventas.sqlite.db")
	cursor = conn.cursor()
	
	cursor.execute("SELECT * FROM 'pedidos'")
	
	rows = cursor.fetchall()
	print (len(rows))
	
	conn.commit()
	conn.close()

import sqlite3

conn = sqlite3.connect("basedatos_ventas.sqlite.db")

cursor = conn.cursor()

try:
	cursor.execute("CREATE TABLE pedidos(num_pedido NUMERIC, scarsua NUMERIC, scarpican NUMERIC, sjamyque NUMERIC, sjamyroque NUMERIC, spollo NUMERIC, shumi NUMERIC, scapres NUMERIC, sespina NUMERIC, pre_unidad NUMERIC, cant_totales NUMERIC, tota_pagar NUMERIC)")
except:
	print("la tabla ya esta creada")

pedidos = (1,2,0,3,2,1,0,0,2,25,10,250)

cursor.execute("INSERT INTO pedidos VALUES(? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? )",(pedidos[0],pedidos[1],pedidos[2],pedidos[3],pedidos[4],pedidos[5],pedidos[6],pedidos[7],pedidos[8],pedidos[9],pedidos[10],pedidos[11]))

conn.commit()

conn.close()

sqlchkfila()
