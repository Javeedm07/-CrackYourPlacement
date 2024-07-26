"""
Intuition:
The code aims to remove duplicates from a sorted list in-place. It uses two pointers, `i` and `j`, to traverse the list: `i` marks the position to place unique elements, while `j` scans through the list. 
When a duplicate is found, `j` is incremented; when a new unique element is found, it is placed at the `i`-th position, and both pointers are incremented. The last element is checked and placed if it is 
not a duplicate. Finally, `i` represents the length of the modified list with unique elements.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j < len(nums) - 1:
            if nums[j] == nums[j + 1]:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        if nums[-1] not in nums[:i]:
            nums[i] = nums[-1]
            i += 1
        return i
