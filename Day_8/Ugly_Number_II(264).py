"""
Intuition:
The code defines a function `nthUglyNumber` that generates the n-th ugly number by maintaining a list of ugly numbers and using three pointers (`a`, `b`, `c`) to track 
the multiples of 2, 3, and 5. In each iteration, it calculates the next potential ugly numbers, selects the smallest one, and advances the corresponding pointer(s). 
This ensures the list is populated with increasing ugly numbers, and the n-th ugly number is returned.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [0]*n
        l[0] = 1
        a=b=c=0
        for i in range(1,n):
            l2 = l[a]*2
            l3 = l[b]*3
            l5 = l[c]*5
            l[i] = min(l2, l3, l5)
            if l2 ==l[i]: a+=1
            if l3 ==l[i]: b+=1
            if l5 ==l[i]: c+=1
                
        return l[n-1]
