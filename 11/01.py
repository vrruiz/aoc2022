#!/usr/bin/env python3
import re

class Mono:

    def __init__(self, numero, items = [], operation = '', test = 0, test_true = -1, test_false = -1):
        self.numero = numero
        self.items = items
        self.operation = self.interpretar_operation(operation)
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.throws = []
        self.borrar = []
        self.inspecciones = 0

    def comprobar(self):
        self.throws = []
        for i in range(len(self.items)):
            self.items[i] = self.operacion(self.items[i])  # Operación
            self.items[i] = self.items[i] // 3
            if self.items[i] % self.test == 0:
                self.throws.append([self.test_true, self.items[i]])
            else:
                self.throws.append([self.test_false, self.items[i]])
            self.inspecciones += 1
        self.items = []
        return self.throws

    def recoger(self, item):
        self.items.append(item)

    def operacion(self, old):
        a, op, b = self.operation
        if a == 'old': a = old
        if b == 'old': b = old
        if op == '+':
            return int(a) + int(b)
        elif op == '-':
            return int(a) - int(b)
        elif op == '*':
            return int(a) * int(b)
        elif op == '/':
            return int(a) // int(b)
        return

    def interpretar_operation(self, operation):
        ops = operation.split()
        return ops

# Inicialización
f_reglas = 'input-01.txt'
monos = []
lineas = [linea.strip() for linea in open(f_reglas)]
i = 0
# Lectura de las reglas
while i < len(lineas):
    if lineas[i].startswith('Monkey'):
        items = [int(i) for i in re.findall(r'\d+', lineas[i+1])]
        operation = re.findall(r'new = (.*)', lineas[i+2])[0]
        test = int(re.findall(r'\d+', lineas[i+3])[0])
        test_true = int(re.findall(r'\d+', lineas[i+4])[0])
        test_false = int(re.findall(r'\d+', lineas[i+5])[0])
        monos.append(Mono(len(monos), items, operation, test, test_true, test_false))
        i += 5
    i += 1

# Rondas
rounds = 20
for i in range(rounds):
    for mono in monos:
        # print(mono.numero, mono.items, mono.operation, mono.test, mono.test_true, mono.test_false)
        lanzamientos = mono.comprobar()
        # print(mono.numero, lanzamientos)
        for lanzamiento in lanzamientos:
            monos[lanzamiento[0]].recoger(lanzamiento[1])
for mono in monos:
    print(f"Monkey {mono.numero} inspected items {mono.inspecciones} times.")
veces = [mono.inspecciones for mono in monos]
veces.sort(reverse=True)
resultado = veces[0] * veces[1]
print(f"What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?\nAnswer: {resultado}")
