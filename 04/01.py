#!/usr/bin/env python3

secciones = [linea.strip() for linea in open('input-01.txt')]

parejas = 0
for seccion in secciones:
    numeros = [set(range(int(a),int(b)+1)) for a, b in [sec.split('-') for sec in seccion.split(',')]]
    if numeros[1].issubset(numeros[0]) or numeros[0].issubset(numeros[1]):
        parejas += 1
print(f"In how many assignment pairs does one range fully contain the other?\nAnswer: {parejas}")