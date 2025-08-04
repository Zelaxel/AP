import networkx as nx

def solve(input_list):
    num_solutions = 0
    all_paths = [] # Cada camino es una lista de nodos del recorrido tomado. 

    g = nx.Graph() 
    for path in input_list:
        nodos = path.split('-')
        g.add_edge(nodos[0],nodos[1])

    def valid(solution):
        current = solution[-1]
        if current.islower() and current in solution[:-1]: # Se repite una caverna pequeña.
            return False
        return True
    
    def dfs(solution):
        nonlocal num_solutions
        if valid(solution):
            current = solution[-1] # Tomamos el último nodo del camino.
            if current == 'end': # Llegó al final de la cueva.
                num_solutions += 1
                all_paths.append(solution)
            else: # Explora otros caminos.
                for n in g.neighbors(current):
                    dfs(solution + [n])
    
    dfs(['start']) # Empieza el recorrido en el 'start'.

    return num_solutions, all_paths

