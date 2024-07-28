"""
Intuition:
The code sorts an array of 0s, 1s, and 2s using the Dutch National Flag algorithm. It maintains three pointers: `low` for the next position of 0, `mid` for the current element, and `high` for the next position of 2. 
It iterates through the array, swapping elements to their correct positions: moving 0s to the beginning, 2s to the end, and leaving 1s in the middle. This ensures the array is sorted in a single pass.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
