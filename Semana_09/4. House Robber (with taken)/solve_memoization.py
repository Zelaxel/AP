# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_memoization(items):
    mem = {}
    taken = []

    def t(n):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        # ...
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools
        if n not in mem:
            if n < 0:
                r = 0
            else:
                r = max(t(n-2)+items[n], t(n-1))
            mem[n] = r
        return mem[n]
        
    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        table = list(mem.values())[2:]
        ben = table[-1]
        for i in range(len(table)-1, -1, -1):
            if table[i] == ben and(i == 0 or  table[i-1] != ben):
                taken.append(i+1)
                ben = ben - items[i]

    n = len(items) - 1    
    max_benefit = t(n)
    
    fill_taken()
    taken.sort()
    
    return max_benefit, taken
