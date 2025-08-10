from solve import *

first_line = input().split()
num_lines = int(first_line[0])

input_list = []
for j in range(num_lines):
    input_list.append(input())

solution = solve(input_list)

print(solution)