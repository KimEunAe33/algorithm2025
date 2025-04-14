'''
binary tree
parent: i
left: 2 * i  +1
right: 2 * i + 2
root from 0
parent: i // 2 of child

example)
a
b b
cc cc
dddd dddd 
change to list structure, then
a b, b c c, c c d d, d d, d d, d d

'''
# min -> root -> change -> min -> root -> change ...

def tournament_sort(arr):
    n = len(arr)
    leaf_size = 1
    while leaf_size < n:
        leaf_size *= 2
    tree = [float('inf')] * (2 * leaf_size - 1)
    
    for i in range(n):
        tree[leaf_size - 1 + i] = arr[i]
    
    for i in range(leaf_size - 2, -1, -1):
        left = tree[2 * i + 1]
        right = tree[2 * i + 2]
        tree[i] = min(left, right) 

    for j in range(n):
        min_index = 0
        for i in range(n):
            if tree[leaf_size-1 + i] == tree[min_index]:
                min_index = leaf_size-1 + i
        
        arr[j]=tree[min_index]
        tree[min_index] = float('inf')  

        while min_index > 0:
            parent_index = (min_index - 1) // 2
            left = tree[2 * parent_index + 1]
            right = tree[2 * parent_index + 2]
            tree[parent_index] = min(left, right) 
            min_index = parent_index