"""
Intuition:
This Python function `subarraySum` counts the number of subarrays in a list `nums` whose sum equals `k`. It uses a prefix sum and a hashmap (`prefix_map`) to store the
frequency of prefix sums encountered. For each element, it checks if the difference between the current prefix sum and `k` exists in the hashmap, which indicates that 
a subarray with the sum `k` has been found, and increments the count accordingly.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  
        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            count += prefix_map.get(diff, 0)
            prefix_map[prefix_sum] = 1 + prefix_map.get(prefix_sum, 0)
        return count
