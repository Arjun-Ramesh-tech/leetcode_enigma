class Solution:
    def isUgly(self, n: int) -> bool:
        if n ==0:
            return False
        for i in [2,3,5]:
            rem = n%i
            while rem==0:
                n = n//i
                rem = n%i
        if n==1:
            return True
        return False
        
