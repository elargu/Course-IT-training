#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import requests
import json

"""
try:
	r = requests.get("http://api.contenidos.lanacion.com.ar/json/dolar")
	d = r.json()

	print("dia :", d["dolarjsonpCallback"]["Date"])
except:
	print("error")
"""

#r = requests.get("http://api.contenidos.lanacion.com.ar/json/dolar")
#r = requests.get("http://api.contenidos.lanacion.com.ar/json/dolar", hooks={'dolarjsonpCallback': 'Date'})
#r.status_code
#d = r.json()

r = requests.get("https://api.dolarsi.com/api/dolarSiInfo.xml")
d = r.json()
print(d)


#print(dolarjsonpCallback)
