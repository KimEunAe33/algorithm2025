#in-place
def find_min_val_index(arr, check, stability=lambda x:x[0]):
    # if i use min() and index() seperately -> O(n) occurs twice -> sloooooooooow
    val , index = arr[check], 0
    for i in range(check, len(arr)):
        if stability(arr[i]) < stability(val):
            val, index = arr[i], i
    return val, index

def selection_sort(arr, stability=lambda x:x[0]):
    for i in range(0, len(arr)-1):
        min_val, min_index = find_min_val_index(arr, i, stability=lambda x:x[0])
        if(stability(arr[i]) > stability(min_val)):
            arr[min_index] = arr[i]
            arr[i] = min_val
            
        