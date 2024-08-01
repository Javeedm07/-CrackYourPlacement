"""
Intuition:
The code reverses the order of words in a given string `s`. It first splits the string into a list of words using `split()`, which removes any whitespace and 
separates the words. Then, it reverses the list of words using slicing (`[::-1]`). Finally, it joins the reversed list of words back into a single string with 
spaces in between using `join()`, and returns the resulting string. This effectively reverses the order of words in the original string.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        rev = l[::-1]
        ans = " ".join(rev)
        return ans
