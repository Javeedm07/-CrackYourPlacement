"""
Intuition:
This code rotates an (n x n) matrix 90 degrees clockwise in two steps. First, it transposes the matrix by swapping elements across the diagonal (converting rows to 
columns). Second, it reflects the matrix horizontally by swapping elements within each row, effectively completing the 90-degree rotation.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        #Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #Reflection
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
