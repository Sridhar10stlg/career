"""
LeetCode #217: Contains Duplicate

Problem:
Given an integer array nums, return True if any value appears more than
once in the array, otherwise return False.

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

Examples:
Input: nums = [1, 2, 3, 3]
Output: True

```
Input: nums = [1, 2, 3, 4]
Output: False
```

Approach:
Use a hash set to track numbers that have already been seen.

```
Iterate through the array:
- If the current number is already in the set, a duplicate exists,
  so return True immediately.
- Otherwise, add the number to the set.

If the iteration completes without finding any duplicates,
return False.
```

Complexity:
Time: O(n)
Space: O(n)

Patterns:
- Hash Set
- Existence Check
- Early Return
"""
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        containsDuplicate = False
        numsDict = {}
        for number in nums:
            if number not in numsDict:
                numsDict[number] = 1
            else:
                numsDict[number] += 1
                containsDuplicate = True
                return containsDuplicate
        print(numsDict)
        return containsDuplicate
