"""
Intuition:
This code implements a binary search algorithm to find a target value in a rotated sorted array. It starts with `left` and `right` pointers at the array's ends and 
calculates the `mid` index. It checks if the `mid` element matches the target, then determines which half of the array is sorted to decide whether to search the left 
or right half. If the target is found, it returns the index; otherwise, it returns `-1`.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
