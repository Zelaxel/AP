def solve(items, capacity):
    taken = []
    value = 0
    
    fraccioned_items = []
    for i in range(len(items)):
        fraccioned_items.append(items[i][0]/items[i][1])
    sorted_items = fraccioned_items.copy()
    sorted_items.sort(reverse=True)
    
    actual_capacity = 0
    value = 0
    for item in sorted_items:
        
        index = None
        for i in range(len(fraccioned_items)):
            if fraccioned_items[i] == item and (i + 1) not in taken:
                index = i
        
        if items[index][1] + actual_capacity <= capacity:
            taken.append(index + 1)
            actual_capacity += items[index][1]
            value += items[index][0]
        
        if actual_capacity == capacity:
            break
    
    return taken, value
