def bubble_sort(arr):
    length = len(arr)
    check = 0
    while check < length:
        for i in range(0, length-check-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        check += 1