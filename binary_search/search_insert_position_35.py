class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while(i<=j):
            middle = int((i+j)/2)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                j = middle - 1
            else:
                i = middle + 1
        return i    
