import networkx as nx
from sys import maxsize as infinite
from collections import namedtuple

Solution = namedtuple("Solution", ["steps", "distance"])

def solve(graph, u, v):
    solutions_list = []
    all_solutions = []
    
    # DFS.
    def dfs(steps, distance):
        current = steps[-1]
        for node in graph.neighbors(current):
            if node == v:
                all_solutions.append(Solution(steps+[node], distance + graph[current][node]["weight"]))
            elif node not in steps:
                dfs(steps+[node], distance + graph[current][node]["weight"])
    
    dfs([u], 0)
    
    # Se busca la distancia mínima.
    min = infinite
    for solution in all_solutions:
        if solution.distance < min:
            min = solution.distance
    
    # Se añade a la lista las soluciones mínima.
    for solution in all_solutions:
        if solution.distance == min:
            solutions_list.append(solution.steps)
    
    return solutions_list
    