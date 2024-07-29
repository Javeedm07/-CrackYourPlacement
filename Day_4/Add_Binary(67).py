"""
Intuition:
The code converts two binary strings `a` and `b` into integers using base 2 conversion. It then adds these integers together. The result is converted back to a binary 
string using the `bin()` function, and the `[2:]` slice is used to remove the '0b' prefix from the binary representation, returning the final binary sum as a string.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return (bin(int(a, 2) + int(b, 2)))[2:]
