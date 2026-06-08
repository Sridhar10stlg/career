"""
LeetCode #1: Two Sum

Problem:
Given an array of integers nums and an integer target, return the
indices i and j such that nums[i] + nums[j] == target and i != j.

```
You may assume that every input has exactly one pair of indices
i and j that satisfy the condition.

Return the answer with the smaller index first.
```

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.

Examples:
Input:
nums = [3,4,5,6], target = 7

```
Output:
[0,1]

Explanation:
nums[0] + nums[1] == 7

Input:
nums = [4,5,6], target = 10

Output:
[0,2]

Input:
nums = [5,5], target = 10

Output:
[0,1]
```

Approach:
Create a hash map that stores each number and its index.

```
First pass:
- Store every number and its index in the hash map.

Second pass:
- For each number, calculate the complement:
  complement = target - current_number
- Check if the complement exists in the hash map.
- Ensure the complement's index is different from the current index.
- Return the pair of indices.
```

Complexity:
Time: O(n)
Space: O(n)

Patterns:
- Hash Map
- Lookup Table
- Complement Search
"""

from typing import List

# Your Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        lenOfNums = len(nums)


        for i in range(lenOfNums):
            numsMap[nums[i]] = i

        for i in range(lenOfNums):
            otherN = target - nums[i]

            if otherN in numsMap and numsMap[otherN] != i:
                return [i, numsMap[otherN]]

'''
# Alternative Optimized Solution

class OptimizedSolution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
    numsMap = {}


        for i, num in enumerate(nums):
            complement = target - num

            if complement in numsMap:
                return [numsMap[complement], i]

            numsMap[num] = i


if **name** == "**main**":
solution = Solution()
optimized = OptimizedSolution()


assert solution.twoSum([3, 4, 5, 6], 7) == [0, 1]
assert solution.twoSum([4, 5, 6], 10) == [0, 2]
assert solution.twoSum([5, 5], 10) == [0, 1]

assert optimized.twoSum([3, 4, 5, 6], 7) == [0, 1]
assert optimized.twoSum([4, 5, 6], 10) == [0, 2]
assert optimized.twoSum([5, 5], 10) == [0, 1]

print("All tests passed!")


'''
