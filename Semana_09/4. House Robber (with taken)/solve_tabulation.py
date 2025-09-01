# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = []
    taken = []
    
    def fill_table():
        # Primera fase: Rellenamos la lista 'table' con las
        # soluciones de todos los subproblemas (o sea, los
        # beneficios que puede conseguir el ladrón).
        # ...
        
        table.append(items[0])
        table.append(max(items[0],items[1]))
        for n in range(2, len(items)):
            table.append(max(table[n-2] + items[n], table[n-1]))
        
    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        t = table
        b = table[-1]
        i = len(table)-1
        while i > 0 and b > 0:
            if t[i] == b and (i == 0 or t[i] != t[i-1]):
                taken.insert(0,i+1)
                b = b-items[i]
            i-=1
        
    fill_table()
    fill_taken()
    
    return table[-1], taken
