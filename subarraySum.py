from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    running_total = 0
    lookup_table = {0: 1}
    
    for x in nums:
        running_total += x
        
        # We need: running_total - previous_total = target
        # Therefore: previous_total = running_total - target
        needed_total = running_total - k
        
        if needed_total in lookup_table:
            count += lookup_table[needed_total]
            
        # Store the current running_total in the dictionary
        if running_total in lookup_table:
            lookup_table[running_total] += 1
        else:
            lookup_table[running_total] = 1
            
    return count

print (subarraySum([28,54,7,-70,22,65,-6], 100))