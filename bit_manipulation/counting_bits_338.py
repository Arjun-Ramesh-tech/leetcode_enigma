from collections import Counter
class Solution:
    def countBits(self, n: int) -> List[int]:
        result_arr = [0]* (n+1)
        result_arr[0] = 0
        if n == 0:
            return result_arr
        result_arr[1] = 1
        for i in range(2,n+1):
            if i%2 ==0:
                result_arr[i] = result_arr[i//2]
            else:
                result_arr[i] = result_arr[i-1] + 1
            result_arr[i]
        return result_arr
