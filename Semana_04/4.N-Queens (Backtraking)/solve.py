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

    def valid(solution):
        """Chequea que la solución sea valida."""
        for i in range(len(solution)-1):
            for j in range(i+1,len(solution)):
                if (solution[i] == solution[j]) or (j-i == abs(solution[j]-solution[i])): # Chequea que no haya 2 reinas por diagonal o por diagonal.
                    return False
        return True

    def bkt(solution):
        """Backstraking."""
        if valid(solution): # Comprueba si es valida. 
            if len(solution) == num_queens: # Lo añade a la lista.
                solutions_list.append(solution)
            else: # Recorre la rama.
                for i in range(num_queens):
                    bkt(solution+[i])
    
    # Primera combinación.
    bkt([])
        
    return solutions_list
