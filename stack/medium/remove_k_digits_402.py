class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        count = 0
        for i in num:
            if count == 0:
                stack.append(i)
                count += 1
                continue
            while count>0 and int(stack[-1])>int(i) and k > 0:
                stack.pop()
                k -= 1
                count -= 1
            stack.append(i)
            count += 1
        while count>0 and int(stack[-1])>int(i) and k > 0:
            stack.pop()
            k -= 1
            count -= 1
        return ''.join(stack[:count-k]).lstrip("0") or "0"
