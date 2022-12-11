#!/usr/bin/env python3

class Cpu():

    ciclos = {
        'noop' : 1,
        'addx' : 2
    }

    def __init__(self, instrucciones = [], depurar=False):
        self.instrucciones = instrucciones
        self.registros = { 'x' : 1 }
        self.ciclo = 0
        self.puntero = -1
        self.seguir = True
        self.espera_ciclo = -1
        self.espera_puntero = -1
        self.fuerza = []
        self.ver_depurar = depurar

    def ejecutar(self):
        seguir = True
        while seguir == True:
            self.ciclo += 1
            if self.ciclo == 20 or (self.ciclo - 20) % 40 == 0:
                # Mostrar fuerza señal
                self.fuerza.append(self.ciclo * self.registros['x'])
                self.depurar()
            if self.espera_ciclo > 0:
                # Instrucción en espera
                if self.espera_ciclo == self.ciclo:
                    # Ejecutar
                    self.interpretar(self.puntero)
                    self.espera_ciclo = -1
            else:
                # Leer nueva instrucción
                self.puntero += 1
                if self.puntero == len(self.instrucciones):
                    # Final de programa
                    seguir = False
                else:
                    ciclos = self.ciclos[self.instrucciones[self.puntero][0]]
                    if ciclos > 1:
                        # Esperar
                        self.espera_ciclo = self.ciclo + ciclos - 1
                    else:
                        # Ejecutar
                        self.interpretar(self.puntero)
            self.depurar()

    def interpretar(self, puntero):
        # self.depurar()
        instruccion, args = self.instrucciones[puntero][0], self.instrucciones[puntero][1:]
        if instruccion == 'noop':
            pass
        elif instruccion == 'addx':
            self.registros['x'] += int(args[0])
        # self.depurar()

    def depurar(self):
        if self.ver_depurar and self.puntero < len(self.instrucciones):
            print(self.ciclo, self.puntero, self.instrucciones[self.puntero], self.registros)

# Lectura de instrucciones
f_instrucciones = 'input-01.txt'
instrucciones = []
for linea in open(f_instrucciones):
    instrucciones.append(linea.strip().split())
cpu = Cpu(instrucciones)
cpu.ejecutar()
suma = sum(cpu.fuerza)
print(f"What is the sum of these six signal strengths?\nAnswer: {suma}")
