"""
Intuition:
This code defines a method `findPair` to check if there exists a pair of elements in the sorted array `arr` with a difference of `x`. It uses a two-pointer technique: 
`i` starts at the beginning and `j` starts at the next element. If the difference between `arr[j]` and `arr[i]` equals `x` and `i` is not equal to `j`, it returns 
1 (indicating such a pair exists). If the difference is less than `x`, it increments `j` to increase the difference; if the difference is greater, it increments `i` 
to decrease the difference. If no such pair is found, it returns -1.
"""

class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        arr.sort()
        i, j = 0, 1
        while i < n and j < n:
            diff = arr[j] - arr[i]
            if diff == x and i != j:
                return 1
            elif diff < x:
                j += 1
            else:
                i += 1
        return -1
