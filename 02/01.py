#!/usr/bin/env python3

ppt = [
    [ 3, 0, 6],
    [ 6, 3, 0],
    [ 0, 6, 3],
]

cual = ['Piedra', 'Papel', 'Tijera']

total = 0
for linea in open('input-01.txt'):
    jugador_a, jugador_b = linea.strip().split()
    ja = ord(jugador_a) - ord('A')
    jb = ord(jugador_b) - ord('X')
    # print(cual[ja], cual[jb], (jb + 1) + ppt[jb][ja])
    total += (jb + 1) + ppt[jb][ja]
print(f"What would your total score be if everything goes exactly according to your strategy guide?\nAnswer:{total}")