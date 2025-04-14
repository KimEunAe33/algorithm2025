'''
https://www.youtube.com/watch?v=3OSeSd2EYkw 
'''
'''
input [3, 2, 1, 5] then
[3, gap] -> [gap, 3] -> [2, 3] -> [2, gap, 3, gap] 
-> [gap, 2,gap, 3] -> [1,2,gap,3] -> [1, gap, 2, gap, 3,gap] 
-> [1, gap, 2, gap, 3, 5] -> [1, gap, 2, gap, 3, gap, 5, gap] 
by binary search.
then I think this will perform same work. adding gap with insertion of element.
g -> g 3 g -> g 2 g 3 g -> g 1 g 2 g 3 g -> g 1 g 2 g 3 g 5 g

'''
def binary_search(gaps2, value, stability=lambda x:x[0]):
    left = 0
    right = len(gaps2)
    while left < right:
        middle = (left + right) // 2
        if stability(gaps2[middle]) > stability(value):
            right = middle
        else:
            left = middle + 1
    return left

def insert_gaps(arr, gaps, index):
    element = arr[index]
    gaps2 = []
    for i in range(len(gaps)):
        if gaps[i] != [None,-1]:
            gaps2.append(gaps[i])
    place = binary_search(gaps2, element, stability=lambda x:x[0])

    gaps[2*place:2*place+1] = [[None,-1], element, [None,-1]]

def library_sort(arr, stability=lambda x:x[0]):
    n = len(arr)
    gaps = [[None, -1]] 
    for i in range(n):
        insert_gaps(arr, gaps, i) 

    index = 0
    for i in range(len(gaps)):
        if stability(gaps[i]) != None:
            arr[index] = gaps[i] 
            index += 1
