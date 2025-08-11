#!/usr/bin/env python
# -*- coding: utf -8 -*-

def solve(input_list, voltage):
    solution_list = []
    modulos = []

    # Programa tu código aquí.
    # ...

    # Convertimos los inputs a lista de listas de enteros.
    for modulo in input_list:
        lista = modulo.split(' ')
        lista[0] = int(lista[0])
        lista[1] = int(lista[1])
        modulos.append(lista)

    best = len(modulos)

    def dfs(cargador):
        nonlocal best
        nonlocal solution_list

        current = [0,0]
        if len(cargador) > 0:
            current = cargador[-1]

        if current[1] == voltage and len(cargador) <= best and cargador not in solution_list:
            if len(cargador) < best:
                best = len(cargador)
                solution_list = []
            solution_list.append(cargador)
        else:
            for modulo in modulos:
                if modulo[0] == current[1] and modulo not in cargador:
                    dfs(cargador + [modulo])


    dfs([])

    return solution_list

