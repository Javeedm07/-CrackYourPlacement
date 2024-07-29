"""
Intuition:
The code converts two binary strings `a` and `b` into integers using base 2 conversion. It then adds these integers together. The result is converted back to a binary 
string using the `bin()` function, and the `[2:]` slice is used to remove the '0b' prefix from the binary representation, returning the final binary sum as a string.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return (bin(int(a, 2) + int(b, 2)))[2:]

"""
Intuition:
The code defines helper functions to convert binary strings to integers (`to_int`) and integers to binary strings (`to_bin`). The `addBinary` function uses 
these helpers to convert binary strings to integers, add them, and convert the result back to a binary string.
"""
class Solution:
    def to_int(self, n):
        # n = str(n)
        ans = 0
        for i in range(len(n)):
            ans += int(n[len(n) - 1 - i]) * (2 ** i)
        return ans

    def to_bin(self, n):
        if n == 0:
            return "0"
        ans = ""
        while n > 0:
            ans = str(n % 2) + ans
            n = n // 2
        return ans

    def addBinary(self, a: str, b: str) -> str:
        ans = self.to_int(a) + self.to_int(b)
        return self.to_bin(ans)
