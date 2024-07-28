"""
Intuition:
The code finds all unique quadruplets in a list that sum to a given target. It first sorts the list, then uses two nested loops to fix the first two numbers and 
two pointers to find pairs of the remaining numbers that sum to the target. If the sum matches the target, the quadruplet is added to a set to ensure uniqueness.
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l = set()
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                a = j + 1
                b = len(nums) - 1
                while(a < b):
                    s = nums[i] + nums[j] + nums[a] + nums[b]
                    if s > target:
                        b -= 1
                    elif s < target:
                        a += 1
                    else:
                        l.add((nums[i], nums[j], nums[a], nums[b]))
                        a += 1
                        b -= 1
        return l
