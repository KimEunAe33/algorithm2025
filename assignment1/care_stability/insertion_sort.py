def insertion_sort(arr, stability=lambda x:x[0]):
    key = 1
    while key < len(arr):
        key_value = arr[key]
        check = key-1
        while check>=0 and stability(arr[check]) > stability(key_value):
            arr[check+1] = arr[check]
            check -= 1
        arr[check+1] = key_value
        key += 1
    return arr
