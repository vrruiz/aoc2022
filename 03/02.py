#!/usr/bin/env python3

def prioridad(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27

elementos = [linea.strip() for linea in open('input-01.txt')]
assert (len(elementos) % 3 == 0)
saltos = len(elementos) // 3

suma = 0
for i in range(saltos):
    grupo = elementos[(i*3):(i*3)+3]
    comun = set(grupo[0]).intersection(set(grupo[1])).intersection(set(grupo[2]))
    assert (len(comun) == 1)
    elemento = list(comun)[0]
    suma += prioridad(elemento)
print(f"What is the sum of the priorities of those item types?\nAnswer: {suma}")