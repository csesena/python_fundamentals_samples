d = {'a': 1, 'b': 2}

# Core ops: O(1) avg
d['c'] = 3                # Set/insert
print(d.get('a', 0))      # Get or default (no KeyError)
print(d.pop('b'))         # Remove + return

# Iteration
for k, v in d.items():    # Key-value pairs
    print(k, v)
for k in d:               # Keys only
    pass

from collections import defaultdict
from typing import List

dd = defaultdict(str)
dd['a'] = '1'
dd['v'] = '2'
dd[(1,2)] = 'value'
print(dd)

if ('value' in dd.values()):
    print("Value exists")

print (dd.get('t', 0))


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            print (seen[complement], i)
            return [seen[complement], i]
        seen[num] = i 
    return []

nums = [3,2,4]
twoSum(nums, 6)