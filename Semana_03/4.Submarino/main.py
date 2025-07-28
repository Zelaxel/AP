from solve import solve
first_line = input().split()
num_lines  = int(first_line[0])

input_list = []
for j in range(num_lines):
    input_list.append(input())

num_solutions, solutions_list = solve(input_list)

# VPL output

solutions_list.sort()
solutions_list.sort(key=len)

for sublist in solutions_list:
    print(sublist)

print(num_solutions)