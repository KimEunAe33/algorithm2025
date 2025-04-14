# divide & conquere 
# in-place
import random

def divide(arr, start, end, stability=lambda x:x[0]):
    pivot_index = random.randint(start, end)  
    # not like introsort, it doesn't have recursive depth
    # so python recursive error occured. So I changed the way setting pivot
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]  
    pivot = arr[end]
    i = start - 1 
    for j in range(start, end): 
        if stability(arr[j]) <= stability(pivot): 
            i += 1  
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1 

def recurse_quick(arr, start, end):
    if start < end:
        pivot = divide(arr, start, end, stability=lambda x:x[0])
        recurse_quick(arr, start, pivot-1)
        recurse_quick(arr, pivot+1, end)

def quick_sort(arr, stability=lambda x:x[0]):
    n = len(arr)
    recurse_quick(arr, 0, n-1)
    