"""
Intuition:
The code finds the longest common prefix among a list of strings. It first sorts the list by length, taking the shortest string as the initial prefix. It then 
iterates through the remaining strings, updating the prefix by comparing characters and shortening it if necessary. The process continues until the longest common 
prefix is determined and returned.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        ans = strs[0]
        for i in range(1, len(strs)):
            s = ""
            for j in range(len(ans)):
                if ans[j] == (strs[i])[j]:
                    s += ans[j]
                else:
                    ans = s
                    break
        return ans
