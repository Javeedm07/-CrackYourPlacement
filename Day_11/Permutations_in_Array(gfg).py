"""
Intuition:
This code defines a method `isPossible` to check if for each pair of elements from two arrays `arr1` and `arr2`, the sum is at least `k`. It sorts `arr1` in 
ascending order and `arr2` in descending order. Then, it iterates through the arrays, checking if the sum of corresponding elements is less than `k`. If any pair's 
sum is less than `k`, it returns `False`; otherwise, it returns `True` if all pairs meet the condition.
"""

class Solution:
    def isPossible(self, k, arr1, arr2):
        arr1.sort()
        arr2.sort(reverse = True)
        for i in range(len(arr1)):
            if arr1[i] + arr2[i] < k:
                return False
        return True
