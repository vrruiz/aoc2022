#!/usr/bin/env python3

def prioridad(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27

suma = 0
for linea in open('input-01.txt'):
    mitad1 = linea[len(linea)//2:]
    mitad2 = linea[:len(linea)//2]
    comun = set(mitad1).intersection(set(mitad2))
    assert (len(comun) == 1)
    elemento = list(comun)[0]
    suma += prioridad(elemento)
print(f"What is the sum of the priorities of those item types?\nAnswer: {suma}")