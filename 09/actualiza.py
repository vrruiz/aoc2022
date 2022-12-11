#!/usr/bin/env python3

def signo(x):
    if x >= 0:
        return 1
    elif x < 0:
        return -1

def actualiza_t(posiciones):
    dif_x = posiciones['H'][0] - posiciones['T'][0]
    dif_y = posiciones['H'][1] - posiciones['T'][1]
    if dif_x == 0 and dif_y == 0:
        # La posición de H y T es la misma
        return posiciones
    elif dif_x == 0 or dif_y == 0:
        # T está arriba, abajo, izquierda o derecha
        if abs(dif_x) > 1:
            posiciones['T'][0] = posiciones['T'][0] + 1 * signo(dif_x)
        elif abs(dif_y) > 1:
            posiciones['T'][1] = posiciones['T'][1] + 1 * signo(dif_y)
    else:
        if abs(dif_x) == 1 and abs(dif_y) == 1:
            # Esquinas
            return posiciones
        elif abs(dif_x) + abs(dif_y) in [3,4]:
            # Diagonal (esquinas +1 o +2)
            posiciones['T'][0] = posiciones['T'][0] + 1 * signo(dif_x)
            posiciones['T'][1] = posiciones['T'][1] + 1 * signo(dif_y)
        else:
            print(f"Posición no soportada: {posiciones}")
    return posiciones

if __name__ == '__main__':
    assert actualiza_t({'H':[0,0],'T':[0,0]}) == {'H':[0,0],'T':[0,0]} # Superposición
    assert actualiza_t({'H':[0,0],'T':[1,0]}) == {'H':[0,0],'T':[1,0]} # Derecha 1
    assert actualiza_t({'H':[0,0],'T':[0,1]}) == {'H':[0,0],'T':[0,1]} # Abajo 1
    assert actualiza_t({'H':[1,0],'T':[0,0]}) == {'H':[1,0],'T':[0,0]} # Izquierda 1
    assert actualiza_t({'H':[0,1],'T':[0,0]}) == {'H':[0,1],'T':[0,0]} # Arriba 1

    assert actualiza_t({'H':[0,0],'T':[2,0]}) == {'H':[0,0],'T':[1,0]} # Derecha 2
    assert actualiza_t({'H':[0,0],'T':[0,2]}) == {'H':[0,0],'T':[0,1]} # Abajo 2
    assert actualiza_t({'H':[2,0],'T':[0,0]}) == {'H':[2,0],'T':[1,0]} # Izquierda 2
    assert actualiza_t({'H':[0,2],'T':[0,0]}) == {'H':[0,2],'T':[0,1]} # Arriba

    assert actualiza_t({'H':[1,1],'T':[0,0]}) == {'H':[1,1],'T':[0,0]} # Esquina sup-izq 1
    assert actualiza_t({'H':[1,1],'T':[2,0]}) == {'H':[1,1],'T':[2,0]} # Esquina sup-der 1
    assert actualiza_t({'H':[1,1],'T':[0,2]}) == {'H':[1,1],'T':[0,2]} # Esquina inf-izq 1
    assert actualiza_t({'H':[1,1],'T':[2,2]}) == {'H':[1,1],'T':[2,2]} # Esquina inf-der 1

    assert actualiza_t({'H':[2,2],'T':[0,1]}) == {'H':[2,2],'T':[1,2]} # Diagonal sup-izq 2
    assert actualiza_t({'H':[2,2],'T':[4,1]}) == {'H':[2,2],'T':[3,2]} # Diagonal sup-der 2
    assert actualiza_t({'H':[2,2],'T':[0,3]}) == {'H':[2,2],'T':[1,2]} # Diagonal inf-izq 2
    assert actualiza_t({'H':[2,2],'T':[4,3]}) == {'H':[2,2],'T':[3,2]} # Diagonal inf-izq 2

    assert actualiza_t({'H':[2,2],'T':[0,0]}) == {'H':[2,2],'T':[1,1]} # Diagonal inf-izq 3
    assert actualiza_t({'H':[2,2],'T':[4,0]}) == {'H':[2,2],'T':[3,1]} # Diagonal sup-der 3
    assert actualiza_t({'H':[2,2],'T':[0,4]}) == {'H':[2,2],'T':[1,3]} # Diagonal inf-izq 3
    assert actualiza_t({'H':[2,2],'T':[4,4]}) == {'H':[2,2],'T':[3,3]} # Diagonal inf-izq 3



