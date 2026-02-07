from typing import List

def longestConsecutive(nums: List[int]) -> int:
    nums = sorted(list(set(nums)))
    max_length = 0
    length = 0 if len(nums) == 0 else 1
    for i,num in enumerate(nums):
        print (i, num, " / length: ", length)
        if (len(nums) > i+1 and num + 1 == nums[i+1]):
            length += 1
        else:
            max_length = max(max_length, length)
            length = 1
    return max_length

#print (longestConsecutive([100,4,200,1,3,2]))
#print (longestConsecutive([1,2,6,7,8]))
print (longestConsecutive([100,4,200,1,3,2]))
