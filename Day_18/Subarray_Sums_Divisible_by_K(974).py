"""
Intuition:
This Python function `subarraysDivByK` counts the number of subarrays in a list `nums` whose sum is divisible by `k`. It uses a prefix sum and a hashmap (`prefix_map`) 
to track the frequency of remainders when the prefix sum is divided by `k`. By checking the current remainder against the hashmap, the function identifies subarrays 
with sums divisible by `k` and increments the count accordingly.
"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  
        
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0:  
                mod += k
            if mod in prefix_map:
                count += prefix_map[mod]
                prefix_map[mod] += 1
            else:
                prefix_map[mod] = 1
        return count
