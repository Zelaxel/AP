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
    for combination in My_Iterator(num_queens, num_queens).next():

        valid_solution = True

        # Comprueba que ninguna reina comparte eje y.
        for i in range(num_queens):
            if combination[i] in combination[0:i]:
                valid_solution = False
                break
        
        # Se descarta si el requisito anterior no se cumple.
        if not valid_solution:
            continue
        
        # Comprueba que ninguna reina comparte diagonal.
        for i in range(num_queens):
            for j in range(1, num_queens-i):
                if combination[i] == combination[i+j] + j or \
                   combination[i] == combination[i+j] - j:
                    valid_solution = False
                    break

        # Se añade si la solucion es valida.
        if valid_solution:
            solutions_list.append(combination)


    return solutions_list
