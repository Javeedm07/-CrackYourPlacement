"""
Intuition:
This code defines a class `Solution` with two methods. The `backspaceResult` method processes a string `s` by simulating the effect of backspace characters ('#') using 
a stack, removing the last character for each '#'. The `backspaceCompare` method compares two strings `s` and `t` after processing them with `backspaceResult`, 
returning `True` if they are equal and `False` otherwise.
"""

class Solution:
    def backspaceResult(self, s):
        stack = []
        for i in s:
            if i == '#':
                if len(stack) == 0:
                    continue
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = self.backspaceResult(s)
        s2 = self.backspaceResult(t)
        return s1 == s2
