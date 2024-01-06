class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        n = len(nums)
        while(i < n and j < n):
            if i==j and nums[i] !=0:
                i += 1
                j += 1
            elif(nums[i]!=0):
                i += 1
            elif nums[j] == 0:
                j += 1
            else:
                k = nums[i]
                nums[i] = nums[j]
                nums[j] = k
                i += 1
                j += 1        
