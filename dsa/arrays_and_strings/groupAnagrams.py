"""
LeetCode #49: Group Anagrams

Problem:
Given an array of strings strs, group all anagrams together into
sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as
another string, but the order of the characters can be different.

Constraints:
1 <= strs.length <= 1000
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters

Examples:
Input:
strs = ["act", "pots", "tops", "cat", "stop", "hat"]

Output:
    [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

Input:
    strs = ["x"]

Output:
    [["x"]]

Input:
    strs = [""]

Output:
    [[""]]

Approach:
For each string, create a character frequency count array of
length 26 representing the letters 'a' through 'z'.

Convert the frequency array into a tuple so it can be used as
a dictionary key.

Strings that are anagrams will generate the same frequency
tuple, so they will be grouped together in the same list.

Finally, return all grouped values from the dictionary.

Complexity:
Time: O(n * m)

where:
    n = number of strings
    m = average length of each string

Space: O(n * m)

Patterns:
- Hash Map
- Frequency Counting
- Grouping
- Character Signature
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = defaultdict(list)

        for each_string in strs:
            count = [0] * 26

            for letter in each_string:
                letterIndex = ord(letter) - ord('a')
                count[letterIndex] += 1

            resultDict[tuple(count)].append(each_string)

        return list(resultDict.values())

"""
Alternative Solution (Sorting Signature)

class OptimizedSolution:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
groups = defaultdict(list)

    for word in strs:
        signature = ''.join(sorted(word))
        groups[signature].append(word)

    return list(groups.values())

if name == "main":
solution = Solution()
optimized = OptimizedSolution()

result1 = solution.groupAnagrams(
    ["act", "pots", "tops", "cat", "stop", "hat"]
)
assert len(result1) == 3

assert solution.groupAnagrams(["x"]) == [["x"]]
assert solution.groupAnagrams([""]) == [[""]]

result2 = optimized.groupAnagrams(
    ["act", "pots", "tops", "cat", "stop", "hat"]
)
assert len(result2) == 3

assert optimized.groupAnagrams(["x"]) == [["x"]]
assert optimized.groupAnagrams([""]) == [[""]]

print("All tests passed!")
"""
"""
Additional Notes:

Your solution is actually the optimal solution for this problem.

Character Count Signature:
Time: O(n * m)
Space: O(n * m)

Sorting Signature:
Time: O(n * m log m)
Space: O(n * m)

Since sorting each word costs O(m log m), your frequency-count
approach is asymptotically faster and is the preferred solution
when the input consists of lowercase English letters.
"""