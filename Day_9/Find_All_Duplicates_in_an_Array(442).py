"""
Intuition:
The code defines a function `findDuplicates` that finds all duplicate elements in a list `nums`. It uses a set `s` to track unique elements as it iterates through the 
list. If an element is already in the set, it is appended to the result list `ans`. Finally, it returns the list of duplicates.
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for i in nums:
            if i in s:
                ans.append(i)
            else:
                s.add(i)
        return ans
