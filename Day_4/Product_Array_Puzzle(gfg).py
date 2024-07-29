"""
Intuition:
This code computes the product of all elements in an array except the current element for each position, handling zeros specially. It calculates the total product 
of all elements and the product of non-zero elements separately. Then, it iterates through the array to adjust each position based on the presence of zeros: 
if there is exactly one zero, the output for that position is the product of non-zero elements; otherwise, the output is zero. For non-zero elements, it divides 
the total product by the current element to get the product of all other elements.
"""

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        prod = 1
        prod2 = 1
        c = 0
        for i in nums:
            if i != 0:
                prod2 *= i #product without zeroes
            else:
                c += 1
            prod *= i #entire product
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if c == 1:
                    nums[i] = prod2
                else:
                    nums[i] = 0
                continue  
            nums[i] = prod // nums[i]
        return nums
