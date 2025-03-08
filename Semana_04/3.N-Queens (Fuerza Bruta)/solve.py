from my_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    # solve it here!
    """Verifica la validez"""
    def valid(solution):
        for i in range(len(solution)-1):
            for j in range(i+1, len(solution)):
                if (solution[i] == solution[j]) or (j-i == abs(solution[j]-solution[i])): # Chequea que no haya 2 reinas por fila y que no haya 2 reinas por diagonal.
                    return False
        return True

    for combination in My_Iterator(num_queens, num_queens).next(): # Comprueba todas las combinaciones.
        if valid(combination):
            solutions_list.append(combination)

    return solutions_list
