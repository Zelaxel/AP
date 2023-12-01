from solve import *

first_line = input().split()
num_queens = int(first_line[0])

solutions_list = solve(num_queens)

for solution in solutions_list:
    print(solution)

# No lo pone en el ejecicio pero añadí un poco
# de código para escribir un fichero de texto y 
# ver el número de combinaciones totales.
with open("combinations.txt", "w") as file:
    for solution in solutions_list:
        file.write(f"{solution}\n")
    file.write(f"\n{len(solutions_list)} combinaciones totales!!!")
file.close()
print("done!")
