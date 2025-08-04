def solve(items):
    
    def merge(left, mid, right):
        A = items[left:mid]
        B = items[mid:right]
        i = 0
        j = 0

        for k in range(left, right):

            if i == len(A):
                items[k] = B[j]
                j+=1
            elif j == len(B):
                items[k] = A[i]
                i+=1
            else:
                if A[i] < B[j]:
                    items[k] = A[i]
                    i+=1
                else:
                    items[k] = B[j]
                    j+=1

    def merge_sort(left, right):
        if left < right:
            mid = (left+right)//2
            merge_sort(left,mid)
            merge_sort(mid+1,right)
            merge(left, mid+1, right+1)


    merge_sort(0,len(items)-1)
