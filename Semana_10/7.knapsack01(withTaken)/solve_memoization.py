def solve_memoization(items, capacity):
    taken = []
    mem={}

    def t(n,w):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools
        # ...
        
        key = (n,w)
        
        if key not in mem:
            if n < 0 or w == 0:
                r = 0
            elif items[n].weight > w:
                r = t(n-1, w)
            else:
                r = max(t(n-1, w), t(n-1, w-items[n].weight)+items[n].value)
            mem[key] = r
        return mem[key]

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de los items elegidos.
        # ...
        
        values = list(mem.values())
        ben = values[-1]
        for i in range(len(values)-1, -1, -1):
            if values[i] <= ben and (i == 0 or values[i-1] != ben):
                ben = items[i].value
                taken.append(i)
            
        

    n = len(items)-1

    max_benefit = t(n,capacity)
    fill_taken()

    return max_benefit, taken
    