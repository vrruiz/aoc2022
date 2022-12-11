#!/usr/bin/env python3
from actualiza import actualiza_t

f_posicion = 'input-test-position.txt'
f_movimientos = 'input-01.txt'

posiciones = {
    'H' : [-1,-1],
    'T' : [-1,-1],
}
num_linea = 0
for linea in open(f_posicion):
    linea = linea.strip()
    for letra in posiciones.keys():
        pos = linea.find('H')
        if pos >= 0:
            posiciones['H'] = [pos, num_linea]
    num_linea += 1
posiciones['T'] = posiciones['H'].copy()

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
    anterior = posiciones.copy()
    for i in range(pasos):
        for n in range(2):
            posiciones['H'][n] += cambios[direccion][n]
        posiciones = actualiza_t(posiciones)
        if posiciones['T'] not in cola:
            cola.append(posiciones['T'].copy())
    # print(direccion, pasos, posiciones)
visitas = len(cola)
print("How many positions does the tail of the rope visit at least once?")
print(f"Answer: {visitas}")
