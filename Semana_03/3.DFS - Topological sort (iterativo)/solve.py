import networkx as nx
from simple_stack import Stack

def dfs_topological_sort(graph):
    """
    Compute one topological sort of the given graph.
    """
    
    # La solucion que retorna esta función es un diccionario de Python.
    #   * La clave del diccionario es el número del nodo
    #   * El valor es el orden topologico asignado a ese nodo
    # 
    # Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
    #                    3 ---> 2 ---> 1
    # ... el orden topologico es:
    #                El vértice 3 va en la primera posición
    #                El vértice 2 en la segunda posición
    #                El vértice 1 en la tercera posición
    # Con lo que debemos devolver un diccionario con este contenido:
    #     {1: 3, 2: 2, 3: 1}

    N = graph.number_of_nodes()
    
    visibleNodes = set()  # En este ejercicio utilizamos un set
                          # para recordar los nodos visibles
    order = {}

    # solve it here! ------------------------------------------------
    S = Stack()

    def dfs_iterative(u):
        nonlocal N
        #  1. Añade código aqui
        #  ...
        S.push(u)
        while not S.isEmpty():
            # En vez de sacarlo de la pila lo observa.
            current = S.peek()
            have_visible_nodes = False
            for node in graph.neighbors(current):
                if node not in visibleNodes:
                    have_visible_nodes = True
                    visibleNodes.add(node)
                    S.push(node)
            # Lo saca de la pila si no tiene vecinos visibles.
            if not have_visible_nodes:
                order[S.pop()] = N
                N -= 1

    #  2. Añade código también aqui
    #  ...
    for node in list(graph.nodes):
        if node not in visibleNodes:
            visibleNodes.add(node)
            dfs_iterative(node)
        
    return order
