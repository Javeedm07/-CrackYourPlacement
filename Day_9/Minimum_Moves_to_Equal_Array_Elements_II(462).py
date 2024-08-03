"""
Intuition:
The code defines a function `minMoves2` that calculates the minimum number of moves required to make all elements in the list `nums` equal, where a move is defined as 
incrementing or decrementing an element by 1. It first sorts the list and uses the median (`x1`) as the target value for minimizing the sum of absolute differences. If 
the length of `nums` is odd, it also considers the element before the median (`x2`) and returns the minimum cost between these two medians.
"""

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        x1 = nums[length // 2]
        ans1 = 0
        for i in nums:
            ans1 += abs(x1 - i)
        if length % 2 == 1:
            ans2 = 0
            x2 = nums[length // 2 - 1]
            for i in nums:
                ans2 += abs(x2 - i)
            return min(ans1, ans2)
        return ans1
