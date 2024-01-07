class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 
        for ele in nums:
            if ele>=0:
                break
            i += 1
        j = i - 1
        n = len(nums)
        result_arr = []
        while(j >=0 and i < n):
            if nums[j]**2 > nums[i]**2:
                result_arr.append(nums[i]**2)
                i += 1
            else:
                result_arr.append(nums[j]**2)
                j -= 1
        while j>=0:
            result_arr.append(nums[j]**2)
            j -= 1
        while i < n:
            result_arr.append(nums[i]**2)
            i += 1
        return result_arr


        
