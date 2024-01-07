class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0 
        j = x
        while(i <= j):
            middle = int((i + j)/2)
            if middle**2 == x:
                return middle
            elif middle**2 > x:
                j = middle - 1
            else:
                i  = middle + 1
        return i-1

        
