class Solution:
    def tribonacci(self, n: int) -> int:
        memory = {0:0,1:1,2:1}
        if n <=2:
            return memory[n]
        def trib_check(n):
            if n in memory:
                return memory[n]
            p = trib_check(n-1) + trib_check(n-2) + trib_check(n-3)
            memory[n] = p
            return p
        return trib_check(n)
        
