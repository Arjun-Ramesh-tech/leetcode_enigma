class Solution:
    def checkStairs(self,n):
        if n in self.hash_value.keys():
            return self.hash_value[n]
        if n == 0:
            return 1
        elif n < 0:
            return 0 
        k = self.checkStairs(n-1) + self.checkStairs(n-2)
        self.hash_value[n] = k
        return k
    def climbStairs(self, n: int) -> int:
        self.hash_value = {}
        return self.checkStairs(n)            
        
