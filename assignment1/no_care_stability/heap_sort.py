# index 0, root is the most biggest one

def max_heapify(arr,n,i):
    root = i # root index 0
    left = 2* i+1
    right = 2*i + 2

    if left < n and arr[left] > arr[root]:
        root = left
    if right < n and arr[right] > arr[root]:
        root = right
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        max_heapify(arr,n,root)

def heap_sort(arr):
   n = len(arr)
   for i in range(n//2-1, -1, -1):
       max_heapify(arr,n, i)
   for i in range(n-1, 0, -1):
       arr[0], arr[i] = arr[i], arr[0]
       max_heapify(arr,i, 0)