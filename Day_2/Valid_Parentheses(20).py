"""
Intuition:
The code checks if a string of brackets is valid using a stack. It pushes opening brackets onto the stack and pops them when a matching closing bracket is found. If any unmatched closing bracket or 
leftover opening brackets remain, the string is invalid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        braces = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for i in s:
            if i in braces:
                stack.append(i)
            elif stack and i == braces[stack.pop()]:
                continue
            else:
                return False
        if len(stack) != 0:
            return False
        return True
