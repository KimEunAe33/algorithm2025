import math
from heap_sort import heap_sort 

def insertion_sort_t(arr, start, end, stability=lambda x:x[0]):
    key = start + 1
    while key <= end:
        key_value = arr[key]
        check = key - 1
        while check >= start and stability(arr[check]) > stability(key_value):
            arr[check + 1] = arr[check]
            check -= 1
        arr[check + 1] = key_value
        key += 1
        
def divide(arr, start, end, stability=lambda x:x[0]):
    pivot = arr[end]  
    i = start - 1 
    for j in range(start, end): 
        if stability(arr[j]) <= stability(pivot): 
            i += 1  
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1 

def recurse_intro(arr, start, end, recursive_depth, stability=lambda x:x[0]):
    if end-start <= 16: # insertion_sort
        insertion_sort_t(arr, start, end, stability=lambda x:x[0])
    elif recursive_depth == 0: # heap_sort
        work_heap = arr[start:end+1]
        heap_sort(work_heap, key=lambda x:x[0])
        arr[start:end+1] = work_heap
    else: # list size > 16
        pivot = divide(arr, start, end, stability=lambda x:x[0])
        recurse_intro(arr, start, pivot, recursive_depth-1, stability=lambda x:x[0])
        recurse_intro(arr, pivot+1, end, recursive_depth-1, stability=lambda x:x[0])

def introsort(arr, stability=lambda x:x[0]):
   recursive_depth = int(2*math.log2(len(arr)))
   recurse_intro(arr, 0, len(arr)-1, recursive_depth, stability=lambda x:x[0])
   
