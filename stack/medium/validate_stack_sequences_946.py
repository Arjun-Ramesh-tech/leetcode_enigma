class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i,j = 0,0
        m,n = len(pushed),len(popped)
        while(i<m and j <n):
            if len(stack) == 0:
                stack.append(pushed[i])
                i += 1
                continue
            if len(stack) > 0 and j<n and popped[j] == stack[-1]:
                stack.pop()
                j += 1
                continue
            if j<n and popped[j] != stack[-1]:
                stack.append(pushed[i])
                i += 1
                continue
        while j<n and popped[j]==stack[-1]:
            stack.pop()
            j += 1
        if len(stack)==0 and i==m and j ==n:
            return 1
        return 0

