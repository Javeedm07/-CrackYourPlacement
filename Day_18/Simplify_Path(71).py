"""
Intuition:
The `simplifyPath` function converts an absolute file path into its simplest form by handling "." (current directory), ".." (parent directory), and redundant slashes. 
It uses a stack to track directory names, popping the stack for ".." and ignoring "." or empty strings. Finally, it returns the simplified path by joining the stack 
elements with slashes.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')
        for dir in directories:
            if dir == '.' or not dir:
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return '/' + '/'.join(stack)
