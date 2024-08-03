"""
Intuition:
The code defines a function `setZeroes` that sets entire rows and columns to zero if any element in those rows or columns is zero. It first iterates through the matrix 
to identify all the positions of zeros, storing them in a list `V`. Then, for each position in `V`, it sets all elements in the corresponding row and column to zero.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        V = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    V.append((i, j))
        for row, col in V:
            matrix[row] = [0] * m
            for i in range(n):
                matrix[i][col] = 0
