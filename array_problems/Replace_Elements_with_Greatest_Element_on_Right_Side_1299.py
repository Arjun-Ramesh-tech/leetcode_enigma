import math
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        n = len(arr)-2
        max_value = arr[-1]
        while(n>=0):
            ans.insert(0,max_value)
            if max_value < arr[n]:
                max_value = arr[n]
            n -= 1
        return ans
