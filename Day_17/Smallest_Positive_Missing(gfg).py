"""
Intuition:
This code finds the smallest missing positive number in a sorted array. It starts with `mis = 1` and iterates through the sorted array. For each element that matches 
`mis`, it increments `mis` by 1. After the loop, `mis` will be the first missing positive number in the array.
"""

class Solution:
    def missingNumber(self,arr,n):
        arr.sort()
        mis = 1
        for i in range(0, len(arr)):
            if arr[i] == mis:
                mis += 1
        return mis
