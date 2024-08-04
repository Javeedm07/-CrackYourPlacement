"""
Intuition:
This code defines a method nextGreaterElement that finds the next greater element for each element in nums1 within nums2. It iterates through each element in nums2 
and for each, searches the subsequent elements for the next greater element, storing the results in a hashmap (hmap). If no greater element is found, it stores -1. 
Finally, it constructs and returns a list (ans) by looking up each element of nums1 in the hashmap.
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    hmap[nums2[i]] = nums2[j]
                    break
                hmap[nums2[i]] = -1
        hmap[nums2[-1]] = -1
        ans = []
        for i in nums1:
            ans.append(hmap[i])
        return ans
