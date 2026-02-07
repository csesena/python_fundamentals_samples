from typing import List

# QuickSort O(n log n) average case, O(n^2) worst case
def quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)


# MergeSort O(n log n)
def mergesort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]

# Python sort() O(n log n) Timsort
print ("Sorted by Python sort(): ",sorted([1,2,3,4,5,6,7,8,9,10]))

# Quicksort O(n log n) average case, O(n^2) worst case
print("Quicksort: ",quicksort([1,2,3,4,5,6,7,8,9,10]))

# MergeSort O(n log n)
print("Mergesort: ",mergesort([1,2,3,4,5,6,7,8,9,10]))





def sortColors(nums: List[int]) -> None:
    counts = [0, 0 ,0]
    for num in nums:
        counts[num] += 1
    i = 0
    for c in range(3):
        print ("c: ", c)
        for _ in range(counts[c]):
            print ("_ : ", _)    
            print ("i: ", i)
            nums[i] = c
            i += 1
    return nums

print (sortColors([2,2,1,0,2,1,0,0,1,2]))
