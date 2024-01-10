class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        n = len(s)
        total = values.get(s[-1])
        for i in range(n-2,-1,-1):
            if values.get(s[i])< values.get(s[i+1]):
                total -= values.get(s[i])
            else:
                total += values.get(s[i])
        return total

        
