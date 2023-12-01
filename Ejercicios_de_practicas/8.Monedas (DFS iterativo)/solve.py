from sys import maxsize as infinite
from collections import namedtuple
from simple_stack import Stack

Solution = namedtuple("Solution", ["index", "taken", "value", "taked"])

def solve(coins, change):
    solutions_list = []
    all_solutions = []
    
    pila = Stack()
    pila.push(Solution(0, [], 0, []))
    
    # DFS.
    while not pila.isEmpty():
        current = pila.pop()
        
        if current.value <= change:
            
            if current.value == change and len(coins) == current.index:
                return current.taken
            elif len(coins) > current.index:
                index = current.index
                taken = current.taken
                value = current.value
                taked = current.taked
                
                izq = Solution(index+1, taken+[index+1], value+coins[index], taked+[coins[index]])
                der = Solution(index+1, taken, value, taked)
                
                pila.push(der)
                pila.push(izq)
    
    return None
