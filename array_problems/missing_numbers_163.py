class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower,upper]]
        result = []
        n = len(nums)
        if not nums[0] == lower:
            result.append([lower,nums[0]-1])
        for i in range(1,n):
            if not (nums[i-1]+1 == nums[i] or nums[i-1] == nums[i]):
                result.append([nums[i-1]+1,nums[i]-1])
        if not nums[n-1] == upper:
            result.append([nums[n-1]+1,upper])
        return result


        
