"""
Intuition:
The code finds all unique triplets in a list that sum to zero. It first sorts the list and then uses a three-pointer approach: fixing one element and using two 
pointers to find pairs that sum to the negative of the fixed element. If a triplet sums to zero, it is added to a set to ensure uniqueness.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = set()
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    l.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return l
