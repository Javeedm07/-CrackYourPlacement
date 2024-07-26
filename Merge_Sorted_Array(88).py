"""
Intuition:
The code merges two sorted arrays, `nums1` and `nums2`, where `nums1` has enough space at the end to hold all elements of `nums2`. First, it copies all 
elements of `nums2` into the remaining positions of `nums1`. Then, it sorts `nums1` to produce a single sorted merged array.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums2)):
            nums1[m + i] = nums2[i]
        nums1.sort()
