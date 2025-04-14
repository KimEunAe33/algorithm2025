def insertion_sort(arr):
    key = 1
    while key < len(arr):
        key_value = arr[key]
        check = key-1
        while check>=0 and arr[check] > key_value:
            arr[check+1] = arr[check]
            check -= 1
        arr[check+1] = key_value
        key += 1
    return arr
