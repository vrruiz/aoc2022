#!/usr/bin/env python3
import re

cargas = []
movimientos = []
for linea in open('input-01.txt'):
    linea = linea.replace('\n', '')
    if linea.startswith('move'):
        movs = [int(s) for s in re.findall('\d+', linea)]
        movimientos.append(movs)
    elif linea != '':
        cargas.append(linea)

num_cols = (len(cargas[0]) - 3) // 4 + 1
num_filas = len(cargas) - 1
cargas_ord = [[] for i in range(num_cols)]
for c in range(num_cols):
    col = 1 + 4 * c
    for f in range(num_filas):
        fila = num_filas - 1 - f
        carga = cargas[fila][col]
        if carga != ' ':
            cargas_ord[c].append(carga)
cargas = cargas_ord

for i in range(len(movimientos)):
    cantidad, desde, a = movimientos[i]
    desde -= 1
    a -= 1
    print(cargas[a], cargas[desde])
    cargas[a].extend(cargas[desde][-cantidad:])
    cargas[desde] = cargas[desde][:-cantidad]
    print(cargas[a], cargas[desde])
    print()
combinacion = ''.join([c[-1] for c in cargas])
print(f"After the rearrangement procedure completes, what crate ends up on top of each stack?\nAnswer: {combinacion}")
