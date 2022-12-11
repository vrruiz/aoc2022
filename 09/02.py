#!/usr/bin/env python3
from actualiza import actualiza_t

f_posicion = 'input-test-position.txt'
f_movimientos = 'input-01.txt'

posiciones = [[-1,-1] for i in range(10)]
h, t = 0, len(posiciones) - 1 # head (cabecera), tail (cola)
num_linea = 0
for linea in open(f_posicion):
    pos = linea.strip().find('H')
    if pos >= 0:
        posiciones[0] = [pos, num_linea]
    num_linea += 1
posiciones = [posiciones[0].copy() for i in range(10)]

cambios = {
    'U': (0, -1),  # Up
    'D': (0, +1),  # Down
    'L': (-1, 0),  # Left
    'R': (+1, 0),  # Right
}
cola = []
for mov in open(f_movimientos):
    direccion, pasos = mov.strip().split()
    pasos = int(pasos)
    for p in range(pasos):
        for n in range(2):
            posiciones[0][n] += cambios[direccion][n]
        for nudo in range(1, len(posiciones)):
            pos = {
                'H' : posiciones[nudo-1].copy(),
                'T' : posiciones[nudo].copy()
            }
            posiciones[nudo] = actualiza_t(pos)['T']
        if posiciones[t] not in cola:
            cola.append(posiciones[t].copy())
visitas = len(cola)
print("How many positions does the tail of the rope visit at least once?")
print(f"Answer: {visitas}")
