#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

r = requests.get("http://contenidos.lanacion.com.ar/json/dolar",stream=True)
print(r.status_code)

dolar = r.json()

print(dolar)
