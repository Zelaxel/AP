from copy import copy
def solve(num_queens):
    """
    Using backtracking compute all the solutions to place the
    given number of queens in a square board.
    
    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions
    
    For example, if num_queens = 4 there are two solutions,
    and it returns:
    solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]
    
    """

    solutions_list = []

    # solve it here!
    def btg(combination):
        """Mediante DFS buscamos la combinacion correcta."""
        
        combination.append(None)

        for pos in range(num_queens):
            
            # probamos las distintas combinaciones
            combination[-1] = pos
            
            # Verificamos que es una combinacion válida.
            if global_check(combination):
                if len(combination) == num_queens:
                    solutions_list.append(copy(combination))
                else:
                    btg(copy(combination))
    
    def global_check(combination):
        """Comprueba que sea una combinación valida de Nx(1...N)."""
        return yaxis_check(combination) and diagonal_check(combination)
    
    def yaxis_check(combination):
        """Comprueba que ninguna reina comparte eje y."""
        for i in range(len(combination)):
            if combination[i] in combination[0:i]:
               return False
        return True
    
    def diagonal_check(combination):
        """Comprueba que ninguna reina comparte diagonal."""
        for i in range(len(combination)):
            for j in range(1, len(combination) - i):
                if combination[i] == combination[i+j] + j or \
                   combination[i] == combination[i+j] - j:
                    return False
        return True
    
    # Primera combinación.
    btg([])
        
    return solutions_list
