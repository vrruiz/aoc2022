#!/usr/bin/env python3
from pprint import pprint
from operator import mul

def caminar(camino, valor, direccion):
    x = 0
    suma = 0
    while x < len(camino):
        suma += 1
        if camino[x] >= valor:
            break
        x += 1
    return suma

def multiplicar(lista):
    no_ceros = [n for n in lista if n > 0]
    if (len(no_ceros) < 1):
        return 0
    r = 1
    for i in no_ceros:
        r *= i
    return r

suma = 0
bosque = []
vistas = []
for linea in open('input-01.txt'):
    bosque.append([int(c) for c in linea.strip()])
    vistas.append([0] * len(bosque[-1]))

parar = False
for y in range(len(bosque)):
    for x in range(len(bosque[y])):
        suma = []
        # print(f"y:{y} x:{x} [{bosque[y][x]}]")
        suma.append(caminar(list(reversed(bosque[y][0:x])), bosque[y][x], "Izquierda"))
        if x+1 < len(bosque[y]):
            suma.append(caminar(bosque[y][x+1:], bosque[y][x], "Derecha"))
        if y > 0:
            suma.append(caminar([bosque[yy][x] for yy in reversed(range(y))], bosque[y][x], "Arriba"))
        if y+1 < len(bosque[y]):
            suma.append(caminar([bosque[yy][x] for yy in range(y+1, len(bosque))], bosque[y][x], "Abajo"))
        vistas[y][x] = multiplicar(suma)
        # print(f"  suma:{suma} {vistas[y][x]}")

# pprint(bosque)
# pprint(vistas)
maximo = 0
for fila in vistas:
    m = max(fila)
    if m > maximo:
        maximo = m
print(f"What is the highest scenic score possible for any tree?\nAnswer: {maximo}") 