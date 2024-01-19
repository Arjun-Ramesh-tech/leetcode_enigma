from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack,n = deque(),len(temperatures)
        result = [0]*n
        for i in range(n):
            if not stack or stack[-1][0]>= temperatures[i]:
                stack.append((temperatures[i],i))
                continue
            while(stack and stack[-1][0] < temperatures[i]):
                k = stack.pop()
                result[k[1]] = i - k[1]
            stack.append((temperatures[i],i))
        return result
