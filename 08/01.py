#!/usr/bin/env python3
from pprint import pprint

def comparar(maximo, anterior, actual, visible):
    if anterior > maximo:
        maximo = anterior
    if maximo < actual:
        visible = 1
    return maximo, visible

bosque = []
alturas = []
for linea in open('input-01.txt'):
    bosque.append([int(c) for c in linea.strip()])
    alturas.append([0] * len(bosque[-1]))

# Izquierda
for y in range(1,len(bosque)-1):
    maximo = -1
    for x in range(1,len(bosque[y])-1):
        maximo, alturas[y][x] = comparar(maximo, bosque[y][x-1], bosque[y][x], alturas[y][x])
# Derecha
for y in range(1,len(bosque)-1):
    maximo = -1
    for x in reversed(range(1,len(bosque[y])-1)):
        maximo, alturas[y][x] = comparar(maximo, bosque[y][x+1], bosque[y][x], alturas[y][x])
# Arriba
for x in range(1,len(bosque[y])-1):
    maximo = -1
    for y in range(1,len(bosque)-1):    
        maximo, alturas[y][x] = comparar(maximo, bosque[y-1][x], bosque[y][x], alturas[y][x])
# Abajo
for x in range(1,len(bosque[y])-1):
    maximo = -1
    for y in reversed(range(1,len(bosque)-1)):
        maximo, alturas[y][x] = comparar(maximo, bosque[y+1][x], bosque[y][x], alturas[y][x])
# Contar
suma = 0
for fila in alturas:
    suma = suma + sum(fila)
suma += len(alturas) * 2 + (len(alturas[0]) - 2) * 2
print(f"How many trees are visible from outside the grid?\nAnswer: {suma}") 