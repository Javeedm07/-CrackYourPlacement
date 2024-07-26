"""
Intuition:
The code moves all zeros in the list `nums` to the end while maintaining the relative order of non-zero elements. It uses two pointers: `i` to mark the position for the next non-zero element and `j` to 
scan through the list. When a non-zero element is found, it swaps it with the element at the `i`-th position, then increments both pointers.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]   
                i += 1
                j += 1     
