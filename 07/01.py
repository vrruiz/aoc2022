#!/usr/bin/env python3

def dicc_claves(dicc, claves):
    elemento = dicc
    for i in claves:
        elemento = elemento[i]
    return elemento

def dir_tamano(dicc, resultados):
    tamano = 0
    for clave in dicc.keys():
        if type(dicc[clave]) == dict:
            t, resultados = dir_tamano(dicc[clave], resultados)
            resultados.append((clave,t))
            tamano += t
        else:
            tamano += dicc[clave]
    return tamano, resultados

directorios = {}
pila = []
for linea in open('input-01.txt'):
    linea = linea.strip()
    if linea.startswith('$ cd'):
        _, comando, directorio = linea.split()
        if directorio == '..':
            pila.pop()
        else:
            padre = dicc_claves(directorios, pila)
            pila.append(directorio)
            padre[directorio] = {}
    elif linea.startswith('$ ls'):
        pass
    elif linea.startswith('dir'):
        pass
    else:
        tamano, fichero = linea.split()
        tamano = int(tamano)
        padre = dicc_claves(directorios, pila)
        padre[fichero] = tamano

resultados = []
tamano, resultados = dir_tamano(directorios, resultados)
total = sum([r[1] for r in resultados if r[1] < 100000])
print(f"What is the sum of the total sizes of those directories?\nAnswer: {total}")
