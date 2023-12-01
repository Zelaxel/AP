from sys import maxsize as infinite
from collections import namedtuple

Solution = namedtuple("Solution", ["index", "taken", "value", "taked"])

def solve(coins, change):
    solutions_list = []
    all_solutions = []
    
    # DFS.
    def dfs(current):
        
        if current.value <= change and (len(current.taked) == 0 or not current.taked[-1] in current.taked[0:-1]):
            
            if current.value == change and len(coins) == current.index:
                all_solutions.append(current.taken)
            elif len(coins) > current.index:
                index = current.index
                taken = current.taken
                value = current.value
                taked = current.taked
                
                izq = Solution(index+1, taken+[index+1], value+coins[index], taked+[coins[index]])
                der = Solution(index+1, taken, value, taked)
                
                dfs(izq)
                dfs(der)

    # Primer dfs.
    dfs(Solution(0, [], 0, []))
    
    # Se buscan los minimos.
    min = infinite
    for solution in all_solutions:
        if len(solution) < min:
            min = len(solution)
    for solution in all_solutions:
        if len(solution) == min:
            solutions_list.append(solution)
    
    return solutions_list
