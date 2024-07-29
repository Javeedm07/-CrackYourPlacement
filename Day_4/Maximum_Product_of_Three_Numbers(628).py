"""
Intuition:
The code sorts the list of numbers and then calculates the product of the three largest numbers and the product of the two smallest numbers with the largest number. 
By comparing these two products, it returns the maximum one. This approach ensures that both the largest positive product and the largest product involving negative 
numbers are considered.
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans1 = nums[-1] * nums[-2] * nums[-3]
        ans2 = nums[0] * nums[1] * nums[-1]
        return max(ans1, ans2)
