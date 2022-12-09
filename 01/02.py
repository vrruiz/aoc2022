#!/usr/bin/env python3

elves = [[]]
for calories_line in open('input-01.txt'):
    if calories_line == '\n':
        elves.append([])
    else:
        elves[len(elves)-1].append(int(calories_line.strip()))
totals = [sum(c) for c in elves]
totals.sort(reverse=True)
print(sum(totals[0:3]))