def solve(items):
    """
    Sort the given list of items in ascending order
    """

    def merge(left, mid, right):
        # solve it here!
        ...
        part1 = items[left:mid]
        part2 = items[mid:right]
        
        for i in range(left, right):
            if len(part1) == 0:
                items[i] = part2.pop(0)
            elif len(part2) == 0:
                items[i] = part1.pop(0)
            else:
                if part1[0] < part2[0]:
                    items[i] = part1.pop(0)
                else:
                    items[i] = part2.pop(0)
    
    def merge_sort(left, right):
        # solve it here!
        ...
        if left < right:
            mid = (left+right)//2
            merge_sort(left, mid)
            merge_sort(mid+1, right)
            merge(left, mid+1, right+1)
    
    merge_sort (0, len(items)-1)
    return
