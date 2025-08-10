import networkx as nx

def solve(input_list):
    num_solutions = 0
    all_paths = []

    G = nx.Graph()
    for edge in input_list:
        nodes = edge.split("-")
        G.add_edge(nodes[0], nodes[1])

    def valid(camino):
        if camino.count("start") > 1:
            return False  
        
        caverna_repetida = None
        for cavern in camino:
            if cavern.islower():
                if camino.count(cavern) > 2:
                    return False
                elif caverna_repetida is None and camino.count(cavern) == 2:
                    caverna_repetida = cavern
                elif caverna_repetida != cavern and camino.count(cavern) == 2:
                    return False
                
        return True

    def dfs(camino):
        nonlocal num_solutions

        if valid(camino):
            current = camino[-1]
            if current == "end": # Final
                num_solutions += 1
                all_paths.append(camino)
            else:
                for cavern in G.neighbors(current):
                    dfs(camino + [cavern])
            
    dfs(["start"])

    return num_solutions, all_paths
