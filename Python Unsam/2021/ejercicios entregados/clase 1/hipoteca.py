# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses=1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra=1000

pmeses_extra=0
nume_mes=0

while saldo > pago_mensual:

    if meses>=61 and meses<=108:
        saldo = saldo*(1+tasa/12)-pago_mensual-pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
        
        print(f'{meses} | $ {total_pagado:0.2f} | $ {saldo:0.2f}')
    else:
        saldo = saldo*(1+tasa/12)-pago_mensual
        total_pagado = total_pagado + pago_mensual
        print(f'{meses} | $ {total_pagado:0.2f} | $ {saldo:0.2f}')
        
    meses=meses+1

if saldo > 0:
    saldo = saldo*(1+tasa/12)
    total_pagado = total_pagado + saldo
    saldo = 0
    print(f'{meses} | $ {total_pagado:0.2f} | $ {saldo:0.2f}')
#porque conservo la lineas que tiene el codigo "meses=meses+1" y "meses=meses-1"??? Puede darse el hipotetico caso de que en el ciclo while el ultimo pago deje al saldo en cero y nunca entre a este if, en ese caso seria necesaria la existencia extricta de la linea "meses=meses-1", por ende "meses=meses+1" tendria que existir en este if . Para mantener la consistencia del codigo se conserva ambas lineas.
    meses=meses+1

meses=meses-1

print('Total pagado:', round(total_pagado, 2))
print('meses:',meses)

