class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        if n <= k:
            return nums[n-1] - nums[0] 
        else:
            mins_value = nums[k-1]
            for i in range(k-1,n):
                if mins_value > nums[i] - nums[i-k+1]:
                    mins_value = nums[i] - nums[i-k+1]
            return mins_value
