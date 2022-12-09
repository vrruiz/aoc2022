#!/usr/bin/env python3

secciones = [linea.strip() for linea in open('input-01.txt')]

intersecciones = 0
for seccion in secciones:
    numeros = [set(range(int(a),int(b)+1)) for a, b in [sec.split('-') for sec in seccion.split(',')]]
    comun = numeros[1].intersection(numeros[0])
    if (len(comun) > 0):
        intersecciones += 1
print(f"In how many assignment pairs does one range fully contain the other?\nAnswer: {intersecciones}")