# gap size: [n/k, n/k^2, n/k^3, ... , 1] -> k == shrink

def comb_sort(arr):
    n = len(arr)
    shrink = 1.3 
    gap = max(1,int(n / shrink))
    check = 0
    
    while gap > 1 or check:
        check = 0
        for i in range(0, n):
            if i+gap >= n:
                break
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                check = 1
        gap = max(1,int(gap / shrink))