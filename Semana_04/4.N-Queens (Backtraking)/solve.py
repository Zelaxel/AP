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
    def bkt(solution):
        if not valid(solution): # Mata la rama ya que no es valida.
            return 
        if len(solution) == num_queens: # Lo añade a la lista.
            solutions_list.append(solution)
        else: # Se recorre el arbol.
            for i in range(num_queens):
                bkt(solution+[i])
    
    """Chequea que la solución sea valida."""
    def valid(solution):
        for i in range(len(solution)-1):
            for j in range(i+1,len(solution)):
                if (solution[i] == solution[j]) or (j-i == abs(solution[j]-solution[i])): # Chequea que no haya 2 reinas por diagonal o por diagonal.
                    return False
        return True
    
    # Primera combinación.
    bkt([])
        
    return solutions_list
