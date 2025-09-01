import numpy as np

def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1,capacity+1), dtype=int)

    def fill_table():
        for n in range(1,len(items)+1):
            for w in range(1,capacity+1):
                weight = items[n-1].weight
                value = items[n-1].value
                if weight <= w:
                    table[n][w] = max(value + table[n-1,w-weight], table[n-1][w])
                else:
                    table[n][w] = table[n-1][w]

    def fill_taken():
        i = len(items)
        k = capacity
        while 0 < i and 0 <= k:
            if table[i][k] != table[i-1][k]:
                taken.insert(0,i)
                k -= items[i-1].weight
            i -= 1

    fill_table()
    fill_taken()
    
    n = len(items)
    
    return table[n][capacity], taken
