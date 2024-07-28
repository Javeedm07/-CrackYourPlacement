"""
Intuition:
The code checks if a given string `s` can be a palindrome by removing at most one character. It first checks if `s` is already a palindrome. If not, it iterates 
through the string comparing characters from both ends. When a mismatch is found, it creates two new strings by removing one of the mismatched characters and checks 
if either of them is a palindrome. If so, it returns `True`; otherwise, it returns `False`.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        i = 0
        j = len(s) - 1
        c = 0
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                ans1 = s[:i] + s[i+1:]
                if ans1 == ans1[::-1]:
                    return True
                ans2 = s[:j] + s[j+1:]
                if ans2 == ans2[::-1]:
                    return  True
                return False
        return True
