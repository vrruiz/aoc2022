#!/usr/bin/env python3
from collections import Counter

long = 14
for linea in open('input-01.txt'):
    linea = linea.strip()
    for i in range(len(linea)-long):
        fin = long+i
        trozo = linea[i:fin]
        contar = max(Counter(trozo).values())
        if contar == 1:
            print(fin)
            break
