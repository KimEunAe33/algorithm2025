# insert + merge


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
        

def merge(arr, l, m, r, stability=lambda x:x[0]):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    l_s = 0
    r_s = 0
    arr_i = l
    while l_s < len(left) and r_s < len(right):
        if stability(left[l_s]) <= stability(right[r_s]):
            arr[arr_i] = left[l_s]
            l_s += 1
        else:
            arr[arr_i] = right[r_s]
            r_s += 1
        arr_i += 1
    while l_s < len(left) or r_s < len(right):
        if l_s < len(left):
            arr[arr_i] = left[l_s]
            l_s +=1
            arr_i+=1
        else:
            arr[arr_i] = right[r_s]
            r_s +=1
            arr_i +=1

def tim_sort(arr, stability=lambda x:x[0]):
    run = 32    # python sort() == time sort 
    n = len(arr)

    for i in range(0, n, run):
        if i+run-1 > n-1:
            insertion_sort_t(arr, i, n - 1,stability=lambda x:x[0])
        else:
            insertion_sort_t(arr, i, i+run-1,stability=lambda x:x[0])

    merging = run
    while merging < n:
        for i in range(0, n, 2 * merging):
            left = i + merging - 1
            right = i + 2 * merging - 1
            if right> n-1:
                right = n-1
            merge(arr, i, left, right, stability=lambda x:x[0])
        merging *= 2
