"""
Intuition:
The code uses Moore's Voting Algorithm to find the majority element in the list `nums`. It maintains a count and a candidate for the majority element, incrementing 
the count when the current element matches the candidate and decrementing it otherwise. When the count reaches zero, a new candidate is selected. The final 
candidate is the majority element.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's majority Algorithm
        count = 0
        for i in range(len(nums)):
            if count == 0:
                count = 1
                majority_element = nums[i]
            elif nums[i] == majority_element:
                count += 1
            else:
                count -= 1
        return majority_element
