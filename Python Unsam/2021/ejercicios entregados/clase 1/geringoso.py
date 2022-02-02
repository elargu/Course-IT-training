cadena='Geringoso'
capadepenapa=''

for c in cadena:
    if c == 'a' or c == 'A':
        capadepenapa=capadepenapa+c+'pa'
    elif c== 'e' or c == 'E':
        capadepenapa=capadepenapa+c+'pe'
    elif c== 'i' or c == 'I':
        capadepenapa=capadepenapa+c+'pi'
    elif c== 'o' or c == 'O':
        capadepenapa=capadepenapa+c+'po'
    elif c== 'u' or c == 'U':
        capadepenapa=capadepenapa+c+'pu'
    else:
        capadepenapa=capadepenapa+c
        
print(capadepenapa)