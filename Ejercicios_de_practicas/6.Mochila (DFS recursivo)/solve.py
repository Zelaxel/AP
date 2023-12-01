from collections import namedtuple

Solution = namedtuple("Solution", ["index", "taken", "value", "room"])

def solve(items, capacity):
    
    best = Solution(0, [], 0, capacity)
    
    def dfs(current):
        
        nonlocal best
        
        if current.room >= 0 and estimated(current) > best.value:
            
            if current.index == len(items):
                best = current
            else:
                index = current.index
                taken = current.taken.copy()
                value = current.value
                room = current.room
                
                izq_solution = Solution(index+1, taken+[index+1], value+items[index][0], room-items[index][1])
                der_solution = Solution(index+1, taken, value, room)
                dfs(izq_solution)
                dfs(der_solution)
    
    def estimated(solution):
        total = solution.value
        for i in range(solution.index, len(items)):
            total += items[i][0]
        return total
    
    dfs(best)
    
    return best.taken, best.value
