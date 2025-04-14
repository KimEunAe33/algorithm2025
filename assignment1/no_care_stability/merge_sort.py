# divide & conquer
def merge_sort(arr):
    if len(arr) == 0 or len(arr) ==1: 
        return arr
    else:
        def conquer(left, right):
            merge = []
            l_check = 0
            r_check = 0
            while True:
                if left[l_check] <= right[r_check]:
                    merge.append(left[l_check])
                    l_check +=1
                else: 
                    merge.append(right[r_check])
                    r_check +=1
                if l_check >= len(left) or r_check >= len(right):
                    break
            merge.extend(left[l_check:])
            merge.extend(right[r_check:])
            return merge
        
        def divide(arr):
            if len(arr) == 0 or len(arr) ==1: 
                return arr
            middle = len(arr)//2
            left = divide(arr[:middle])
            right = divide(arr[middle:])
            return conquer(left, right)
        
        result = divide(arr)
        arr[:] = result