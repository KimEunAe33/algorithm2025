# index 0, root is the most biggest one

def max_heapify(arr,n,i, key=lambda x:x[0]):
    root = i # root index 0
    left = 2* i+1
    right = 2*i + 2

    if left < n and key(arr[left]) > key(arr[root]):
        root = left
    if right < n and key(arr[right]) > key(arr[root]):
        root = right
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        max_heapify(arr,n,root, key=lambda x:x[0])

def heap_sort(arr, key=lambda x:x[0]):
   n = len(arr)
   for i in range(n//2-1, -1, -1):
       max_heapify(arr,n, i, key=lambda x:x[0])
   for i in range(n-1, 0, -1):
       arr[0], arr[i] = arr[i], arr[0]
       max_heapify(arr,i, 0, key=lambda x:x[0])