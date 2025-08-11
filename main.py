from solve import *

first_line = input().split()
num_lines = int(first_line[0])
voltage = int(first_line[1])

input_list = []
for j in range(num_lines):
    input_list.append(input())

try:
    solution_list = solve(input_list, voltage)

    # VPL output

    for sublist in solution_list:
        print(sublist)

    print(len(solution_list), "solutions")

except:
    print("wrong code; exception raised")
