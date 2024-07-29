"""
Intuition:
The code converts a given column number to its corresponding Excel column title. It repeatedly calculates the remainder when the column number is decremented by 1 
and divided by 26, using this remainder to find the corresponding character from `upper`. The process is akin to converting a base-10 number to a base-26 
representation with letters. The result is built by prepending characters to the string `s` until the column number is reduced to zero.
"""

upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while(columnNumber > 0 ):
            rem = (columnNumber - 1) % 26
            s = upper[rem] + s
            columnNumber = (columnNumber - 1) // 26
        return s
