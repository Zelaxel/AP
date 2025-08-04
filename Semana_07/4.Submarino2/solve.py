import networkx as kx
from time import sleep

def solve(input_list):
    num_solutions = 0
    all_paths = []

    G = kx.Graph()

    for path in input_list:
        nodos = path.split("-")
        G.add_edge(nodos[0], nodos[1])

    def valid(solution):
        current = solution[-1]
        if current == "start" and len(solution) > 1: # Se repite el start.
            return False
        
        if solution[0] == "start": # No hay cueva pequeña que se repita.
            if current.islower() and current in solution[:-1]: # Marcamos la cueva pequeña que se repite.
                solution.insert(0,current)

        if current.islower() and solution.count(current) > 1 and current != solution[0]: # Se repite otra cueva pequeña.
            return False
        
        if current.islower() and solution.count(current) > 3 and current == solution[0]: # Se repite mas de una vez la cueva pequeña.
            return False
        
        return True

    def dfs(solution):
        nonlocal num_solutions
        if valid(solution): # Compruebo si es un camino valido.
            current = solution[-1]
            if current == "end": # Compruebo si llegamos al final.
                num_solutions += 1
                if solution[0] != "start":
                    solution.pop(0)
                all_paths.append(solution)
            else: # Exploro el resto de caminos.
                for cave in G.neighbors(current):
                    dfs(solution + [cave])

    dfs(["start"])

    return num_solutions, all_paths