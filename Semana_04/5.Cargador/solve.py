#!/usr/bin/env python
# -*- coding: utf -8 -*-

def solve(input_list, voltage):
    solution_list = []

    # Programa tu código aquí.
    # ...

    # Convertimos la input_list de strings a tuplas.
    for i in range(len(input_list)):
        input_list[i] = input_list[i].split(' ')
        input_list[i][0] = int(input_list[i][0])
        input_list[i][1] = int(input_list[i][1])
        input_list[i] = (input_list[i][0], input_list[i][1])

    # Mejor longitud.
    best = len(input_list)

    def dfs(cargador):
        nonlocal best
        nonlocal solution_list

        current = (0,0)
        if len(cargador) != 0:
            current = cargador[-1]

        # Solución.
        if current[1] == voltage and cargador not in solution_list:
            if len(cargador) < best:
                best = len(cargador)
                solution_list = []
            solution_list.append(cargador)
        # Continuamos.
        else:
            for modulo in input_list:
                if modulo not in cargador and modulo[0] == current[1]:
                    dfs(cargador + [modulo])

    # Primera solución. 
    dfs([])

    return solution_list