#Intuition:
#For each element, check if (target - ith element) is present in the remaining sub array. If yes, return the positions.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums) 
        for i in range(n):
            res=target - nums[i]
            if res in nums[i+1:]:
                return [i,nums[i+1:].index(res)+i+1]
