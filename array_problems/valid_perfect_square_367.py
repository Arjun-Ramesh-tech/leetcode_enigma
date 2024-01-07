class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True
        i = 0
        j = num - 1
        while(i<=j):
            middle = int((i + j)/2)
            if middle**2 == num:
                return True
            elif middle**2 > num:
                j = middle - 1
            else:
                i = middle + 1
        return False
