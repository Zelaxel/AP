import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    # ...
    # Se prepara
    visible = [first_node]
    Q = Queue()
    Q.enqueue(first_node)
    distance[first_node] = 0
    
    # Bucle BFS.
    while not Q.isEmpty():
        current = Q.dequeue()
        for node in graph.neighbors(current):
            if node not in visible:
                visible.append(node)
                distance[node] = distance[current] + 1
                Q.enqueue(node)
    return distance
