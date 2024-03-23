class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, n = [],len(s)
        s = list(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and len(stack) == 0:
                s[i] = ''
            elif s[i] == ')':
                stack.pop()
        for i in stack:
            s[i] = ''
        return ''.join(s)
        
