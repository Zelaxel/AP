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
            weight = items[n].weight
            value = items[n].value
            if n < 0:
                mem[key] = 0
            elif weight > w:
                mem[key] = t(n-1,w)
            else:
                mem [key] = max(t(n-1,w), t(n-1,w-weight)+value)
        return mem[key]
            

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de los items elegidos.
        # ...
        i = len(items)-1
        k = capacity

        while 0 <= i and 0 < k:
            if t(i,k) != t(i-1,k):
                taken.insert(0,i+1)
                k -= items[i].weight
            i-=1
            
        

    n = len(items)-1

    max_benefit = t(n,capacity)
    fill_taken()

    return max_benefit, taken
    