# -><--><-

def cocktail_shaker_sort(arr, key=lambda x:x[0]):
    front = 0
    back = len(arr) - 1
    while front < back:
        # big -> to right
        for i in range(front, back):
            if key(arr[i]) > key(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        back -= 1

        # small -> to left
        for i in range(back, front, -1):
            if key(arr[i]) < key(arr[i - 1]):
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        front += 1
