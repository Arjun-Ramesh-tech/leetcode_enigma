class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                k = stack.pop()
                stack.append(k)
                stack.append(k*2)
            elif i == '+':
                i = stack.pop()
                j = stack.pop()
                stack.append(j)
                stack.append(i)
                stack.append(i+j)
            else:
                stack.append(int(i))
        return sum(stack)
