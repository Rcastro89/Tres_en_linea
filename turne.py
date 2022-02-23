#!/usr/bin/python3

posciciones = {1: 'E', 2: 'E', 3: 'E',
               4: 'E', 5: 'E', 6: 'E',
               7: 'E', 8: 'E', 9: 'E'}


def selec_turne(actualy):
    if actualy == "X":
        return "O"
    else:
        return "X"


def jugada(pos, turno):
    posciciones.update({pos: turno})


def validar_ganador():
    opciones = ["X", "O"]
    gana = [1, 2, 3]
    for op in opciones:
        validar = all(op == posciciones.get(llave) for llave in gana)
        if validar:
            return op
    gana = [4, 5, 6]
    for op in opciones:
        validar = all(op == posciciones.get(llave) for llave in gana)
        if validar:
            return op
    gana = [7, 8, 9]
    for op in opciones:
        validar = all(op == posciciones.get(llave) for llave in gana)
        if validar:
            return op
    gana = [1, 4, 7]
    for op in opciones:
        validar = all(op == posciciones.get(llave) for llave in gana)
        if validar:
            return op
    gana = [2, 5, 8]
    for op in opciones:
        validar = all(op == posciciones.get(llave) for llave in gana)
        if validar:
            return op
    gana = [3, 6, 9]
    for op in opciones:
        validar = all(op == posciciones.get(llave) for llave in gana)
        if validar:
            return op
    gana = [1, 5, 9]
    for op in opciones:
        validar = all(op == posciciones.get(llave) for llave in gana)
        if validar:
            return op
    gana = [3, 5, 7]
    for op in opciones:
        validar = all(op == posciciones.get(llave) for llave in gana)
        if validar:
            return op
    fin = any('E' == posciciones.get(llave) for llave in posciciones.keys())
    if fin == False:
        return 'E'
    return "-1"

