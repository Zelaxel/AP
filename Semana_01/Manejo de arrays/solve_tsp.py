"""La función combina 2 arrays, padre y madre respectivamente, de una foema especifica."""
def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child1 = parent1[lower_bound:upper_bound]
    madre = parent2[upper_bound:] + parent2[:upper_bound]
    for i in madre:
        if i not in parent1[lower_bound:upper_bound]:
            child1.append(i)
    return child1[len(parent1)-lower_bound:] + child1[:len(parent1)-lower_bound]
