"""
LeetCode #347: Top K Frequent Elements

Problem:
Given an integer array nums and an integer k, return the k most
frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Constraints:
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums

Examples:
Input:
nums = [1, 2, 2, 3, 3, 3]
k = 2

Output:
    [2, 3]

Input:
    nums = [7, 7]
    k = 1

Output:
    [7]

Approach:
Count the frequency of each number using a hash map.

Create a bucket array where the index represents the frequency
and each bucket stores the numbers that occur with that frequency.

Place each number into its corresponding frequency bucket.

Traverse the buckets from highest frequency to lowest frequency,
collecting elements until k elements have been gathered.

Complexity:
Time: O(n)
Space: O(n)

Patterns:
- Hash Map
- Bucket Sort
- Frequency Counting
"""

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHash = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for number in nums:
            countHash[number] = countHash.get(number, 0) + 1

        for number, freq in countHash.items():
            bucket[freq].append(number)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])

            if len(result) >= k:
                return result[:k]
        
"""
Alternative Solution (Min Heap)

class OptimizedSolution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]

if name == "main":
solution = Solution()
optimized = OptimizedSolution()

assert set(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2)) == {2, 3}
assert solution.topKFrequent([7, 7], 1) == [7]

assert set(optimized.topKFrequent([1, 2, 2, 3, 3, 3], 2)) == {2, 3}
assert optimized.topKFrequent([7, 7], 1) == [7]

print("All tests passed!")
"""

"""
Additional Notes:

Your solution is the optimal Bucket Sort approach.

Bucket Sort:
Time: O(n)
Space: O(n)

Min Heap:
Time: O(n log k)
Space: O(n)

Since Bucket Sort achieves O(n) time complexity, it is generally
considered the best solution for this problem and is the approach
most commonly expected in interviews after the Hash Map solution.
"""