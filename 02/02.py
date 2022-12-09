#!/usr/bin/env python3

ppt = [
   # Per, Emp, Gan
    [(0,3), (3,1), (6,2)], # Piedra
    [(0,1), (3,2), (6,3)], # Papel
    [(0,2), (3,3), (6,1)], # Tijera
]

cual = ["Piedra", "Papel", "Tijera"]
hay_que = ["Perder", "Empatar", "Ganar"]

total = 0
for linea in open('input-01.txt'):
    el, res = linea.strip().split()
    elemento = ord(el) - ord('A')
    resultado = ord(res) - ord('X')
    puntos, hay_que_usar = ppt[elemento][resultado]
    # print(cual[elemento], hay_que[resultado], "->", cual[hay_que_usar-1], f"{puntos} + {hay_que_usar}")
    total += puntos + hay_que_usar
print(f"What would your total score be if everything goes exactly according to your strategy guide?\nAnswer:{total}")