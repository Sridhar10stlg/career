"""
LeetCode #242: Valid Anagram

Problem:
Given two strings s and t, return True if the two strings are
anagrams of each other, otherwise return False.

```
An anagram is a string that contains the exact same characters as
another string, but the order of the characters can be different.
```

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Examples:
Input: s = "racecar", t = "carrace"
Output: True

```
Input: s = "jar", t = "jam"
Output: False
```

Approach:
Build frequency dictionaries for both strings.

```
First, check whether the lengths of the strings are equal.
If they are not equal, they cannot be anagrams.

Traverse both strings simultaneously and maintain character
frequencies in separate dictionaries. After processing all
characters, compare the dictionaries.

If both dictionaries are identical, the strings are anagrams.
```

Complexity:
Time: O(n)
Space: O(n)

Patterns:
- Hash Map
- Frequency Counting
- String Comparison
"""

from typing import Dict

# Your Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        SDictionary = {}
        TDictionary = {}

        lens, lent = len(s), len(t)

        if lens != lent:
            return False
        else:
            for i in range(0, lens):
                if s[i] not in SDictionary:
                    SDictionary[s[i]] = 1
                else:
                    SDictionary[s[i]] += 1

                if t[i] not in TDictionary:
                    TDictionary[t[i]] = 1
                else:
                    TDictionary[t[i]] += 1

        return SDictionary == TDictionary

'''
# Alternative Optimized Solution

class OptimizedSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
        return False

            count: Dict[str, int] = {}

            for char_s, char_t in zip(s, t):
                count[char_s] = count.get(char_s, 0) + 1
                count[char_t] = count.get(char_t, 0) - 1

            return all(value == 0 for value in count.values())

if **name** == "**main**":
solution = Solution()
optimized = OptimizedSolution()


assert solution.isAnagram("racecar", "carrace") is True
assert solution.isAnagram("jar", "jam") is False
assert solution.isAnagram("anagram", "nagaram") is True
assert solution.isAnagram("rat", "car") is False

assert optimized.isAnagram("racecar", "carrace") is True
assert optimized.isAnagram("jar", "jam") is False
assert optimized.isAnagram("anagram", "nagaram") is True
assert optimized.isAnagram("rat", "car") is False

print("All tests passed!")


"""
'''