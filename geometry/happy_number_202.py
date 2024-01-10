class Solution:
    def isHappy(self, n: int) -> bool:
        seen_values = set()
        while 1:
            seen_values.add(n)
            answer = 0
            while(n>0):
                answer += (n%10)**2
                n = n//10
            if answer ==1:
                return True
            if answer in seen_values:
                return False
            n = answer

