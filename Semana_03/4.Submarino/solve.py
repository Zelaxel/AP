import networkx as nx

def solve(input_list):
    all_paths = [] # Cada camino es una lista de nodos del recorrido tomado. 

    g = nx.Graph() 
    for path in input_list:
        nodos = path.split('-')
        g.add_edge(nodos[0],nodos[1])
    
    def dfs(solution):
        current = solution[-1] # Tomamos el último nodo del camino.
        if current == 'end':
            # Llegó al final de la cueva.
            all_paths.append(solution)
        else:
            # Todavía sigue en la cueva.
            for n in g.neighbors(current):
                if not (n.islower() and n in solution):
                    dfs(solution + [n])
    
    dfs(['start']) # Empieza el recorrido en el 'start'.

    return len(all_paths), all_paths

