"""
Intuition:
The code sorts the list and then uses a sliding window of size M to find the minimum difference between the maximum and minimum values in any M-sized subset. 
It returns the smallest difference found, or -1 if M is greater than N.
"""

class Solution:
    def findMinDiff(self, A, N, M):
        if M > N:
            return -1
        A.sort()
        min_diff = float('inf')
        for i in range(N - M + 1):
            current_diff = A[i + M - 1] - A[i]
            if current_diff < min_diff:
                min_diff = current_diff
        return min_diff
